# internship-task-1-data-cleaning
Data cleaning and transformation task for internee.pk

## Project Overview
This project provides an automated solution to clean and structure raw internship application data. It utilizes Python and the Pandas library to ensure data integrity by removing duplicates and addressing missing values.

## Features
* **Duplicate Removal**: Automatically identifies and removes duplicate records based on `Applicant_ID`.
* **Data Imputation**: 
    * Fills missing `Internship_Duration_Months` with a default value of `3`.
    * Standardizes empty or missing `Skills` fields by replacing them with the label `'Not Specified'`.

## How to Use
1. Clone this repository.
2. Ensure you have `pandas` installed: `pip install pandas`.
3. Run the script: `python main.py`.

## Technologies Used
* **Python**
* **Pandas**
