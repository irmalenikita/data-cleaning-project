# Data-cleaning-project

**Data Cleaning Project**

**Overview**

This project focuses on cleaning a raw dataset using Pandas to ensure it is free from duplicates, missing values, and unnecessary columns. The goal is to make the data structured, consistent, and ready for further analysis.

**Key Objectives**

✅ Remove duplicate records

✅ Standardize categorical values

✅ Format phone numbers correctly

✅ Handle missing values

✅ Drop unnecessary columns

✅ Filter out irrelevant data


**Steps Taken**

**1. Inspecting the Data**

- Checked the dataset’s structure using df.info() to understand column names, data types, and missing values.
- Identified missing values using df.isnull().sum().

**2. Removing Duplicates**

- Dropped duplicate records to ensure data uniqueness.

**3. Dropping Unnecessary Columns**

- Removed irrelevant columns that did not contribute to the analysis.

**4. Cleaning and Formatting Data**

- Last Names: Removed unwanted characters (/, ., _).
- Phone Numbers: Standardized format to XXX-XXX-XXXX by removing special characters and keeping only digits.
- Categorical Values: Converted "Yes/No" responses into "Y/N" for consistency.

**5. Handling Missing Values**

- Replaced 'N/a' and NaN values with an empty string to maintain data integrity.

**6. Filtering Out Unwanted Data**

- Removed rows where "Do_Not_Contact" was "Y" to exclude users who opted out.
- Dropped records with missing phone numbers to ensure data completeness.

**7. Resetting Index**

- After cleaning the data, the index was reset to maintain proper row ordering.
 
**Findings & Outcomes**

- Successfully cleaned the dataset by removing unnecessary data and standardizing key fields.
- Improved data quality, making it ready for further analysis.
- Ensured consistency in phone number formatting and categorical values.
