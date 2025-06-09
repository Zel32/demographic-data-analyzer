# 📊 Demographic Data Analyzer

This project is part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/). It analyzes demographic data from a census dataset and extracts meaningful insights using Python and pandas.

## 🎯 Project Objective

To perform statistical analysis on a dataset containing demographic information and compute various metrics such as average age, educational attainment, income brackets, and employment statistics.

## 📁 Dataset

The dataset used in this project is `adult.data.csv`, originally from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult). It includes features like:

- Age
- Race
- Education
- Hours worked per week
- Occupation
- Salary
- Native country

## 🔍 Key Analyses Performed

The `calculate_demographic_data()` function in `demographic_data_analyzer.py` computes:

- Count of each race represented in the dataset
- Average age of men
- Percentage of individuals with a Bachelor's degree
- Percentage of individuals with and without advanced education (Bachelors, Masters, Doctorate) earning more than 50K
- Minimum number of hours worked per week
- Percentage of people working minimum hours who earn more than 50K
- Country with the highest percentage of people earning more than 50K
- Most common occupation for high earners in India

## 🗂️ Project Structure

- `demographic_data_analyzer.py`: Main script for data processing and statistical calculations
- `test_module.py`: Unit tests that validate each statistical output
- `main.py`: Entry point to run the analysis and execute the test suite

## ▶️ How to Run

1. Ensure you have Python and `pandas` installed.
2. Place `adult.data.csv` in the same directory as the scripts.
3. 3. Run the following command:

```bash
python main.py
