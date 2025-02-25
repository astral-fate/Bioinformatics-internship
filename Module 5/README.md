


Goal: The overall goal of the data cleaning section is to prepare the anti-microbial resistance data for visualization in Tableau. The current data is in a format unsuitable for immediate analysis and visualization.

Problem Identified: The data is inconsistent with a number of issues that are highlighted such as the data in columns with incorrect information. and the removal of the header “Anti-biotic class” that occurs on more than one row.

Data Cleaning and Validation Steps:

Removing Sample ID Headers from Columns C through AQ.

Requirement: The first row of each column is the label "Sample ID" or an empty string.

Steps:

Select the entire sheet, then find the label.

Delete the text, "Sample ID".

Remove the row using the delete operation.

Inspect and remove special characters for string value names

Requirement: There might be some special values within the data that are not correctly written.

Steps:

Inspect and correct the spelling for string data types

Consolidating multi-antibiotic variables to new header names.

Requirement: Multi class antibiotics need to be described


Handling Missing Data:

Requirement: Every cell needs to contain a value, not be blank, especially in numerical and categorical data columns.

Steps:

Select all of the columns in the datasheet

Use “Find what” to find a value in the table

Use the "replace with" selection and type 0.

Press Replace All

Close and see the update with zero’s in all spaces.

Explanation of the choices:

Replacing Empty Cells with Zero (0): The justification for this is to ensure uniformity in all rows so that it will be correctly read during visualizations in Tableau.

Grouping: Consolidating long descriptive text” The video demonstrates with multi-antibiotic class. This is done for brevity and consistency in Tableau and to remove the complexity of multi-words and sentences.

Tool Used:

Microsoft Excel: The video is using Excel to demonstrate data cleaning techniques. This is more like a manually way of correcting all the information one after the other.

Important Note:

## Data cleaning and visualization

1. Fill missing genes with zero
2. Categorize the names of the drugs
