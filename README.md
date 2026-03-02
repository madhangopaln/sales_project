# Sales Aggregation Project

## Objective
Extract total quantities of each item bought per customer aged 18-35.

## Business Rules
- Sales receipt can contain multiple items
- NULL quantity = item not purchased
- Exclude items with total quantity = 0
- Output format: Customer;Age;Item;Quantity

## Setup

pip install -r requirements.txt

## Run

python main.py

## Output
Files generated in /output folder:
- sql_output.csv
- pandas_output.csv

Both solutions are validated to produce identical output.