# Bioinformatics Internship - Antimicrobial Resistance Project

 
 

This repository documents my progress and learnings during a bioinformatics internship. The internship covered a range of essential bioinformatics skills, from data acquisition and preprocessing to advanced genomic analysis and statistical visualization.

## Modules and Key Learnings

| Module | Main Topics Covered | Key Topics | Deliverables |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [Module 1: Data Retrieval and Pre-processing](Module%201) | Introduction to data retrieval and pre-processing techniques for bioinformatics data. | - Understanding public databases (e.g., NCBI). <br> - Data retrieval strategies. <br> - Data cleaning and quality control methods.  | [Link to any scripts, notebooks, or documentation for Module 1]  |
| [Module 2: Data Acquisition and Preprocessing](Module%202) | Focuses on retrieving isolates of pathogenic diseases from publicly available datasets. |  - NCBI database navigation and search. <br> - Identification and retrieval of pathogenic disease isolates.  | [Link to any scripts, notebooks, or documentation for Module 2]  |
| [Module 3: Comprehensive Genome Analysis](Module%203) | Exploration of comprehensive genome analysis techniques | -Functional Annotation <br> - Data analysis methods. | [Link to any scripts, notebooks, or documentation for Module 3] |
| [Module 4: Genomic Insights into Drug Resistance and Mechanisms of Adaptation](Module%204) | Investigating genomic factors related to drug resistance and adaptation mechanisms in microorganisms. | - Identification of drug resistance genes. <br> - Analysis of adaptive mutations. | [Link to any scripts, notebooks, or documentation for Module 4] |
| [Module 5: Statistical Analysis and Visual Representation of Resistome Profile Study](Module%205) | Performing statistical analysis and creating visualizations to understand resistome profiles. | - Statistical methods for analyzing genomic data. <br> - Data visualization techniques (e.g., R, Python libraries).  | [Link to any scripts, notebooks, or documentation for Module 5] |
| [Module 6: Subsystem](Module%206) |This chapter delves into the meaning of Subsystem, and how it influences resistance of Antimicrobial Resistance (AMR) | - What is a subystem <br> - Relationship with AMR.  | [Link to any scripts, notebooks, or documentation for Module 6] |
| [Module 7: Comparative Genome Analysis (Insights into Spread and Transmission)](Module%207) | Using comparative genomics to understand the spread and transmission patterns of microorganisms. | - Phylogenetic analysis. <br> - Identifying transmission pathways.  | [Link to any scripts, notebooks, or documentation for Module 7] |
 
 
## Table of Contents

*   [Introduction](#introduction)
*   [Helpful Resources](#helpful-resources)
*   [Module 1: Data Retrieval and Pre-processing](#module-1-data-retrieval-and-pre-processing)
*   [Module 2: Genome Assembly](#module-2-genome-assembly)
*   [Module 3: Gene Annotation](#module-3-gene-annotation)
*   [Module 4: AMR Analysis and Data Standardization](#module-4-amr-analysis-and-data-standardization)
*   [Module 5: Data Cleaning and Preparation for Visualization](#module-5-data-cleaning-and-preparation-for-visualization)
*   [Module 6: Data Visualization](#module-6-data-visualization)
*   [Module 7: Subsystem](#module-7-subsystem)
*   [Tools and Technologies](#tools-and-technologies)
*   [Overall Project Goals](#overall-project-goals)
*   [Future Directions](#future-directions)
*   [Author](#author)

## Introduction

[Write a brief introductory paragraph here, summarizing the project and its goals.] For instance, you could say, "This project investigates the genomic basis of antimicrobial resistance in _Salmonella enterica_ through data mining, genome analysis, and visualization. We aimed to identify resistance genes, understand their distribution, and create interactive visualizations to explore the relationships between genes, antibiotics, and bacterial strains."

## Helpful Resources

The following resources were helpful for learning and completing the internship:

1.  [https://learn.mongodb.com/learn/learning-path/introduction-to-mongodb](https://learn.mongodb.com/learn/learning-path/introduction-to-mongodb)
2.  [https://learn.mongodb.com/learning-paths/mongodb-python-developer-path](https://learn.mongodb.com/learning-paths/mongodb-python-developer-path)
3.  [https://learn.mongodb.com/courses/pymongoarrow](https://learn.mongodb.com/courses/pymongoarrow)
4.  [https://training.talkpython.fm/courses/details/mongodb-python-quickstart-mongoengine](https://training.talkpython.fm/courses/details/mongodb-python-quickstart-mongoengine)

## Module 1: Data Retrieval and Pre-processing

*   **Search Terms Used:**
    *   `("Salmonella" OR "S.") AND ("typhi" OR "typhoid") AND ("antimicrobial resistance" OR "antibiotic resistance" OR "AMR")`
    *   `"Salmonella enterica" AND "antimicrobial resistance"`

## Module 2: Genome Assembly

A general workflow for AMR monitoring using bioinformatics tools:

**Step 1: Data Collection**

*   Collect bacterial isolates from various sources (e.g., clinical, environmental, animal)
*   Extract genomic DNA from the isolates

**Step 2: Genome Assembly**

*   Use genome assembly tools (e.g., SPAdes, Velvet) to reconstruct the bacterial genome from sequencing data
*   Evaluate assembly quality using metrics (e.g., N50, contig length)

**Step 3: Genome Annotation**

*   Use genome annotation tools (e.g., Prokka, NCBI Genome Annotation) to predict protein-coding genes and functional annotations
*   Integrate annotations with external databases (e.g., CARD, ARG-ANNOT)

*   **Data Sources:**
    *   [https://db.cngb.org/search/sample/?q=PRJNA289090](https://db.cngb.org/search/sample/?q=PRJNA289090)
    *   [https://data.mendeley.com/research-data/?type=DATASET&search=%22Salmonella%20typhi%22%20AND%20%22antimicrobial%20resistance%22](https://data.mendeley.com/research-data/?type=DATASET&search=%22Salmonella%20typhi%22%20AND%20%22antimicrobial%20resistance%22)
    *   [https://www.typhoidgenomics.org/](https://www.typhoidgenomics.org/)
*   **Data Distribution Resources:**
    *   [https://www.ncbi.nlm.nih.gov/pathogens/isolates/#%22Salmonella%20enterica%22%20AND%20%22antimicrobial%20resistance%22](https://www.ncbi.nlm.nih.gov/pathogens/isolates/#%22Salmonella%20enterica%22%20AND%20%22antimicrobial%20resistance%22)
    *   [https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA998920](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA998920)
    *   [https://www.ncbi.nlm.nih.gov/pathogens/isolates/#(%22Salmonella%22%20OR%20%22S.%22)%20AND%20(%22typhi%22%20OR%20%22typhoid%22)%20AND%20(%22antimicrobial%20resistance%22%20OR%20%22antibiotic%20resistance%22%20OR%20%22AMR%22)](https://www.ncbi.nlm.nih.gov/pathogens/isolates/#(%22Salmonella%22%20OR%20%22S.%22)%20AND%20(%22typhi%22%20OR%20%22typhoid%22)%20AND%20(%22antimicrobial%20resistance%22%20OR%20%22antibiotic%20resistance%22%20OR%20%22AMR%22)

    *   Reference: [https://elifesciences.org/articles/85867/figures#content](https://elifesciences.org/articles/85867/figures#content)
*   **Genome Assembly Steps (BV-BRC):**
    1.  Head to [https://www.bv-brc.org/](https://www.bv-brc.org/)
    2.  Go to tools - genome assembly: [https://www.bv-brc.org/app/Assembly2](https://www.bv-brc.org/app/Assembly2)
    3.  Write the name of SRA
    4.  Go to job list: [https://www.bv-brc.org/job/](https://www.bv-brc.org/job/)
    *   **Screenshots (example):**
        ![image](https://github.com/user-attachments/assets/fa7931fe-7062-45e6-a82e-edb5b9dea2a9)
        ![image](https://github.com/user-attachments/assets/a6f99af8-102b-4391-986d-1a33fa85f2b4)

## Module 3: Gene Annotation

*   **Resource Links:**
    *   Genome Assembly: [https://www.bv-brc.org/app/Assembly2](https://www.bv-brc.org/app/Assembly2)
    *   Gene Annotation: [https://www.bv-brc.org/app/Annotation](https://www.bv-brc.org/app/Annotation)
*   **Screenshot (example):**
    ![image](https://github.com/user-attachments/assets/269d22d3-9449-4192-86fd-5a6bbfdaac82)

## Module 4: AMR Analysis and Data Standardization

*   **Resources:**
    *   BV-BRC Workspace:
        *   [https://www.bv-brc.org/workspace/astral\_fate@bvbrc/home/ST1](https://www.bv-brc.org/workspace/astral_fate@bvbrc/home/ST1)
        *   [https://www.bv-brc.org/workspace/astral\_fate@bvbrc/home/S18](https://www.bv-brc.org/workspace/astral_fate@bvbrc/home/S18)
*   **AMR Results Expected:**
    *   AMR GENES
    *   ANTIBIOTICS
    *   ANTIBIOTIC CLASS
    *   CLASSIFICATION (MECHANISM)
    *   PRODUCT

*   **Data Standardization Procedure:**
    *This document outlines the data standardization procedure applied to the dataset, leveraging a pre-defined set of mappings for various columns. The core principle is to ensure consistency and reduce redundancy within the data, facilitating more effective analysis and interpretation.

    *   **Standardization Process:**
        1.  **Loading the Data:** Load from a dataframe, and input CSV file and the dataframe being passed into the loop.
        2.  **Iterating through Columns:** The script iterates through a pre-defined list of columns in the DataFrame. This allows the script to skip any columns that don't need standardization, because of not being in the dictionary.
        3.  **Mapping Application:** For each specified column, the `apply_mapping` function is called.
        4.  **`apply_mapping` Function:**  The `apply_mapping` function checks if the column name exists as a key in the `complete_mapping` dictionary. If the column name is found in the dictionary, the corresponding mapping dictionary is retrieved.
           The function then applies a mapping to each value in the column. It attempts to find the existing value in the mapping dictionary. If a match is found, the value is replaced with the standardized value from the dictionary. Otherwise, the original value remains unchanged.
        5.  **Output:** After processing all specified columns, the standardized DataFrame is saved to a new CSV file.

        **Data Transformation Examples**

        Below are tables illustrating examples of the data transformations applied to key columns. Note that the source data is not provided in this file, so the data in the table is just for demonstrational purposes.

        **1. Gene Standardization**

        | Original Value | Standardized Value |
        |-----------------|----------------------|
        | folA, Dfr      | dfrA                 |
        | dfrA7          | dfrA                 |
        | inhA, fabI      | fabI                 |
        | AcrAB-TolC     | acrAB-tolC           |

        **2. Product Standardization**

        | Original Value                                        | Standardized Value                        |
        |-------------------------------------------------------|-------------------------------------------|
        | Hexose phosphate transport protein UhpT                | UhpT transport protein                  |
        | Translation elongation factor Tu                       | Elongation factor Tu                      |
        | Multidrug efflux system AcrEF-TolC, membrane fusion component AcrE | AcrE efflux pump component             |

        **3. Function Standardization**

        | Original Value                                                        | Standardized Value                                     |
        |-----------------------------------------------------------------------|-------------------------------------------------------|
        | Hydrogen peroxide-inducible genes activator => OxyR                     | OxyR activator                                      |
        | Alanine racemase (EC 5.1.1.1)                                          | Alanine racemase                                      |
        | Translation elongation factor Tu                                        | Elongation factor Tu                                 |
        | MULTISPECIES: type A-1 chloramphenicol O-acetyltransferase          | Chloramphenicol O-acetyltransferase                  |

        **4. Classification Standardization**

        | Original Value                                                                                        | Standardized Value                                      |
        |-------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
        | antibiotic resistant gene variant or mutant,fosfomycin resistance gene                               | fosfomycin resistance gene                              |
        | aminoglycoside resistance gene,antibiotic inactivation enzyme                                        | aminoglycoside resistance gene                              |
        | antibiotic resistant gene variant or mutant,elfamycin resistance gene                               | elfamycin resistance gene                              |
        | efflux pump conferring antibiotic resistance                                                          | efflux pump conferring antibiotic resistance                              |

        **5. Source Organism Standardization**

        | Original Value                               | Standardized Value    |
        |---------------------------------------------|-----------------------|
        | Escherichia coli str. K-12 substr. MC4100 | Escherichia coli      |
        | Escherichia coli str. K-12 substr. MG1655 | Escherichia coli      |
        | Escherichia coli O157:H7 str. Sakai      | Escherichia coli      |
        | Salmonella enterica subsp. enterica serovar Typhimurium str. LT2| Salmonella enterica   |

                **6. Evidence Standardization**

        | Original Value | Standardized Value |
        |-----------------|----------------------|
        | BLAT      | BLAT                 |
        | K-mer Search          | K-mer Search                 |

                **7. Property Standardization**

        | Original Value | Standardized Value |
        |-----------------|----------------------|
        | Antibiotic Resistance      | Antibiotic Resistance                 |

                        **8. Source Standardization**

        | Original Value | Standardized Value |
        |-----------------|----------------------|
        | CARD      | CARD                 |
        | PATRIC         | PATRIC                 |
        | NDARO | NDARO   |

        **9. Numerical Standardization**

        | Original Value | Standardized Value |
        |-----------------|----------------------|
        | 0.0      | unknown                |
        | 0         | unknown                |
        | 80.0      | 80.0          |
        | 100.0         | 100.0                |

    *   **Reduction in Unique Values**
        The standardization process resulted in a significant reduction of unique values:

        | Column Name        | Unique Values (Before) | Unique Values (After) |
        |--------------------|------------------------|-----------------------|
        | Genome Name        | 32                     | 1                     |
        | BRC ID             | 3149                   | 106                   |
        | Source Organism    | 25                     | 12                    |
        | Gene               | 123                    | 111                   |
        | Product            | 103                    | 97                    |
        | Function           | 75                     | 69                    |
        | Classification     | 34                     | 23                    |
        | Subject Coverage   | 29                     | 14                    |
        | Query Coverage     | 13                     | 11                    |
        | Identity           | 20                     | 19                    |

*   **Conclusion:** The data standardization procedure effectively consolidates data and enhances consistency, which facilitates more meaningful analysis.

## Module 5: Data Cleaning and Preparation for Visualization

*   **Goal:**  Prepare the anti-microbial resistance data for visualization in Tableau.
*   **Problems Identified:** Inconsistent data, incorrect information in columns, and removal of the header "Anti-biotic class" that occurs on more than one row.
*   **Data Cleaning and Validation Steps:**
    1.  **Removing Sample ID Headers:**
        *   Requirement:  The first row of each column is the label "Sample ID" or an empty string.
        *   Steps:  Select the entire sheet, find the label, delete the text, and remove the row.
    2.  **Inspect and correct special characters for string value names**
        *   Requirement: There might be some special values within the data that are not correctly written.
        *   Steps: Inspect and correct the spelling for string data types
    3.  **Consolidating multi-antibiotic variables to new header names.**
        *   Requirement: Multi class antibiotics need to be described
    4.  **Handling Missing Data:**
        *   Requirement: Every cell needs to contain a value, not be blank, especially in numerical and categorical data columns.
        *   Steps: Select all columns, use "Find what" to find a blank value, use "replace with" and type 0, then press Replace All.
*   **Explanation of Choices:**
    *   Replacing Empty Cells with Zero (0): Ensures uniformity in all rows.
    *   Grouping: Consolidating long descriptive text for brevity and consistency.
*   **Tool Used:** Microsoft Excel (for manual cleaning)
*   **Important Notes:**
    1.  Fill missing genes with zero
    2.  Categorize the names of the drugs

## Module 6: Data Visualization

*   **Requested Visualizations:**
    *   Gene against Sample ID
    *   Antibiotics class against Sample ID
    *   Antibiotics against Sample ID
    *   Classification against Sample ID
    *   Gene against Antibiotic class
    *   Gene against classification
    *   Antibiotics Class against Classification
*   **Goal:** Plot and visualize the relationship between "Gene", "Antibiotics", “Antibiotics Class”, “Classification” for different strains to get the data in a more understandable way.
*   **Data Visualization Tools:** Tableau and Python.

*   **Tableau Dashboard:**
    *   [https://public.tableau.com/app/profile/fatma.mohammed3602/viz/ARMDashboard\_17404650816940/Dashboard1](https://public.tableau.com/app/profile/fatma.mohammed3602/viz/ARMDashboard_17404650816940/Dashboard1)
        ![image](https://github.com/user-attachments/assets/736f8bf2-968c-4aef-b901-83ce41e38f6b)
*   **Python Virtualization**

    *   **Implications:** The visualizations provide valuable insights into the mechanisms and distribution of antimicrobial resistance across bacterial species. The prevalence of efflux pumps suggests that targeting these mechanisms could be an effective strategy for developing new antimicrobial agents. The species-specific patterns indicate that resistance profiles vary significantly between bacterial groups, which has implications for targeted antimicrobial therapy. The complex network of relationships between genes, products, functions, and classifications demonstrates that antimicrobial resistance is a multifaceted phenomenon that requires comprehensive approaches for effective monitoring and intervention.
    *   ![8\_relationship\_network](https://github.com/user-attachments/assets/7cc04f70-275a-482b-b7cb-0925d454c564)
    *   ![7\_antibiotic\_class\_classification](https://github.com/user-attachments/assets/c5fe8e2c-43e6-407e-8b48-7fa1df055cd7)
    *   ![6\_gene\_classification](https://github.com/user-attachments/assets/5a105a92-f197-4850-aa67-d777d8922871)
    *   ![5\_gene\_antibiotic\_class](https://github.com/user-attachments/assets/b146fc85-a2fc-4e30-b7d1-e4b66e35aa7f)
    *   ![4\_classification\_sample\_id](https://github.com/user-attachments/assets/e670a349-f750-405b-a233-0ffef2326b7a)
    *   ![3\_antibiotics\_sample\_id](https://github.com/user-attachments/assets/9126d386-7896-4d84-b4ea-10ec4c69f698)
    *   ![2\_antibiotics\_class\_sample\_id](https://github.com/user-attachments/assets/386429ca-9f8f-4e31-a875-8123031f666c)
    *   ![1\_gene\_sample\_id](https://github.com/user-attachments/assets/4c8c1d58-04da-4a2f-a218-40f13a79cabe)
    *   ![11\_antibiotics\_count\_by\_classification](https://github.com/user-attachments/assets/27a751a6-0b43-48f0-8885-ebd669f607ed)
    *   ![10\_gene\_count\_by\_antibiotic\_class](https://github.com/user-attachments/assets/1a964ae5-0d86-4ff5-b373-acbf3cd25ffd)

## Module 7: Subsystem

THESE THE DELIVRABLES

## Tools and Technologies

*   SPAdes, Velvet: Genome assembly tools.
*   Prokka, NCBI Genome Annotation: Genome annotation tools.
*   CARD, ARG-ANNOT: Antimicrobial resistance databases.
*   Microsoft Excel: Data cleaning and preparation.
*   Tableau: Interactive data visualization.
*   Python: General purpose programming and data analysis.
*   [Add other tools/libraries used, e.g., R, specific Python libraries]

## Overall Project Goals

*   Develop skills in genomic data analysis, including assembly, annotation, and standardization.
*   Gain experience in identifying and characterizing antimicrobial resistance genes.
*   Master data visualization techniques for exploring relationships between genes, antibiotics, and bacterial strains.
*   Contribute to the understanding of antibiotic resistance mechanisms and transmission.

## Future Directions

*   Further analysis of specific resistance genes and their mechanisms of action.
*   Integration of genomic data with clinical and epidemiological data.
*   Development of predictive models for antimicrobial resistance.

