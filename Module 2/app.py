import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def verify_driver_setup():
    """Verify ChromeDriver installation and permissions."""
    chrome_driver_path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
    
    if not os.path.exists(chrome_driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at: {chrome_driver_path}")
    
    try:
        with open(chrome_driver_path, 'rb') as f:
            pass
        return chrome_driver_path
    except PermissionError:
        raise PermissionError("Permission denied! Try running as administrator")
    except Exception as e:
        raise Exception(f"Error accessing ChromeDriver: {str(e)}")

def get_processed_samples(output_csv):
    """Get list of already processed samples from existing output file."""
    processed_samples = set()
    if os.path.exists(output_csv):
        try:
            with open(output_csv, 'r') as f:
                reader = csv.DictReader(f)
                processed_samples = {row['BioSample'] for row in reader}
        except Exception as e:
            logging.error(f"Error reading existing output file: {e}")
    return processed_samples

def scrape_sra_data(csv_file, output_csv):
    """
    Scrape SRA data from NCBI website based on BioSample IDs.
    Saves results incrementally to prevent data loss.
    """
    # Get already processed samples
    processed_samples = get_processed_samples(output_csv)
    logging.info(f"Found {len(processed_samples)} already processed samples")
    
    try:
        # Verify driver setup
        chrome_driver_path = verify_driver_setup()
        logging.info(f"ChromeDriver found at: {chrome_driver_path}")

        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)

        # Set up Chrome driver service with explicit path
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("Chrome WebDriver initialized successfully")

        # Count total rows for progress tracking
        with open(csv_file, 'r', encoding='utf-8') as f:
            total_rows = sum(1 for row in csv.DictReader(f, delimiter=','))
        logging.info(f"Total samples to process: {total_rows}")

        # Open output file in append mode if it exists, write mode if it doesn't
        file_mode = 'a' if processed_samples else 'w'
        with open(csv_file, 'r', encoding='utf-8') as infile, open(output_csv, file_mode, newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile, delimiter=',')
            fieldnames = ['BioSample', 'SRA', 'Run', '# of Spots', '# of Bases', 'Size', 'Published']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Write header only if creating new file
            if file_mode == 'w':
                writer.writeheader()

            # Process each row
            for index, row in enumerate(reader, 1):
                try:
                    biosample_id = row['BioSample']
                except KeyError as e:
                    logging.error(f"Missing 'BioSample' column in row: {row}")
                    continue  # Skip to next row

                # Skip if already processed
                if biosample_id in processed_samples:
                    logging.info(f"Skipping already processed BioSample: {biosample_id}")
                    continue

                logging.info(f"Processing {index}/{total_rows}: BioSample {biosample_id}")
                
                try:
                    driver.get(f"https://www.ncbi.nlm.nih.gov/biosample/{biosample_id}")
                    time.sleep(2)  # Give the page time to load

                    # Find the SRA link
                    try:
                        sra_link = driver.find_element(By.LINK_TEXT, "SRA")
                        sra_url = sra_link.get_attribute("href")
                        driver.get(sra_url)
                        time.sleep(2)

                         # Extract SRA ID
                        try:
                            sra_title_xpath = "//p[@class='details expand e-hidden']/b/a"
                            sra_text = driver.find_element(By.XPATH, sra_title_xpath).text
                            sra_id = sra_text.split(':')[0]
                        except NoSuchElementException:
                            logging.warning(f"Could not extract SRA ID for {biosample_id}")
                            sra_id = None

                        # Extract Table Data
                        try:
                            #Locate the actual data rows.
                            table = driver.find_element(By.XPATH, "//table[@border='0' and @cellpadding='1' and @cellspacing='0']")
                            table_rows = table.find_elements(By.TAG_NAME, "tbody")
                            
                            if not table_rows:
                                logging.warning("Table does not contain tbody elements. Skipping record")
                                continue
                            #iterate through the rows of the table to grab data
                            for table_row in table_rows:
                                table_cells = table_row.find_elements(By.TAG_NAME, "td") #Get all the cells
                                if len(table_cells) < 5:
                                    logging.warning("table is short on elements, skipping to the next")
                                    continue
                                #Now get text from the column
                                run = table_cells[0].text
                                spots = table_cells[1].text
                                bases = table_cells[2].text
                                size = table_cells[3].text
                                published = table_cells[4].text

                                #Process if size is applicable
                                if size:
                                    #Process sizes into sizes into size_mb
                                    if "Mb" in size:
                                        size_mb = float(size.replace("Mb", ""))
                                    elif "Gb" in size:
                                        size_mb = float(size.replace("Gb", "")) * 1024
                                    else:
                                        size_mb = None # setting this to none so as to not let bad data come in
                                     #Write if its applicable
                                    if size_mb is not None and 300 <= size_mb <= 2048 and sra_id:
                                        writer.writerow({
                                            'BioSample': biosample_id,
                                            'SRA': sra_id,
                                            'Run': run,
                                            '# of Spots': spots,
                                            '# of Bases': bases,
                                            'Size': size,
                                            'Published': published
                                            })
                                        outfile.flush()  # Force write to disk
                                        processed_samples.add(biosample_id)
                                        logging.info(f"Found SRA: {sra_id}, Run: {run}, Size: {size_mb} Mb")
                                    else:
                                        logging.info(f"  SRA found, but size {size_mb} Mb is outside the specified range (300MB - 2GB).")


                        except NoSuchElementException:
                            logging.warning("SRA Table was not found on page")
                            continue


                    except Exception as e:
                        logging.error(f"   No SRA link found for {biosample_id} OR error navigating to it: {e}")

                except Exception as e:
                    logging.error(f"  Error processing {biosample_id}: {e}")

    except Exception as e:
        logging.error(f"Critical error: {str(e)}")
        raise
    
    finally:
        if 'driver' in locals():
            driver.quit()
        logging.info(f"Scraping complete. Processed {len(processed_samples)} samples. Results saved to: {output_csv}")

def main():
    """Main entry point of the script."""
    try:
        # Configure input and output files
        input_csv_file = '4k.csv'  
        output_csv_file = 'sra_data.csv'
        
        # Run the scraper
        scrape_sra_data(input_csv_file, output_csv_file)
        
    except Exception as e:
        logging.error(f"Program failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()