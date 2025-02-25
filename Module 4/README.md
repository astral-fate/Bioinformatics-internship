
## BV-BRC: Bacterial and Viral Bioinformatics Resource Center

https://www.bv-brc.org/workspace/astral_fate@bvbrc/home/ST1
ST-38


https://www.bv-brc.org/workspace/astral_fate@bvbrc/home/S18

AMR RESULTS

• AMR GENES

• ANTIBIOTICS 

• ANTIBIOTIC CLASS

• CLASSIFICATION (MECHANISM)

• PRODUCT



## Data Standardization Procedure

This document outlines the data standardization procedure applied to the provided dataset, leveraging a pre-defined set of mappings for various columns. The core principle is to ensure consistency and reduce redundancy within the data, facilitating more effective analysis and interpretation. The script `data_cleaning.py` utilizes dictionaries to map original values to standardized values, and a function `apply_mapping` is defined to standardize each column based on the keys of the complete_mapping dictionary.

The script begins with dictionaries defined to map from non-standard to standard names based on the values in the dataset. Each dictionary is defined for the following columns: Gene, Product, Function, Classification, Source Organism, Evidence, Property, Source, and numerical data, where many of the numerical columns are standardized.

### Standardization Process

1.  **Loading the Data:** The process begins with a dataframe being created from the input CSV file and the dataframe being passed into the loop.

2.  **Iterating through Columns:** The script iterates through a pre-defined list of columns in the DataFrame. This allows the script to skip any columns that don't need standardization, because of not being in the dictionary.

3.  **Mapping Application:** For each specified column, the `apply_mapping` function is called.

4.  **`apply_mapping` Function:** The `apply_mapping` function checks if the column name exists as a key in the `complete_mapping` dictionary.

    *   If the column name is found in the dictionary, the corresponding mapping dictionary is retrieved.

    *   The function then applies a mapping to each value in the column. It attempts to find the existing value in the mapping dictionary. If a match is found, the value is replaced with the standardized value from the dictionary. Otherwise, the original value remains unchanged.

5.  **Output:** After processing all specified columns, the standardized DataFrame is saved to a new CSV file.

### Data Transformation Examples

Below are tables illustrating examples of the data transformations applied to key columns. This is not an exhaustive list but demonstrates the types of changes made. Note that the source data is not provided in this file, so the data in the table is just for demonstrational purposes. The reduction in unique values listed in the documentation shows the efficiency of the procedure.

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

### Reduction in Unique Values

The documentation you've provided highlights a significant reduction in the number of unique values within several columns. This demonstrates the effectiveness of the standardization process in consolidating data and improving consistency. The reduction in unique values is detailed in the following table:

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

### Conclusion

The data standardization procedure, leveraging pre-defined mappings, effectively consolidates data and enhances consistency across various columns. This improves the data's quality and facilitates more meaningful analysis, which provides more reliable, standardized data.
