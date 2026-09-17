# Dimensional Modeling - Star Schema Design Assignment

## Overview

This assignment is designed to help you redesign a normalized (OLTP) dataset into a star schema suitable for reporting and analysis, using Python and SQL.

## Instructions

1. Open it in VS Code.

2. Implement your code inside `src/main/lab.py`.

3. Run your script and check the output.

4. Take a screenshot of your output, add it to the assignment folder, and compress the whole folder into a zip file for submission. If you created a virtual environment (`.venv`) while working on this, remove it before zipping as it's large and not needed for grading.

## Notes

- Four normalized source tables are provided inside `src/data/`: `customers.csv`, `products.csv`, `orders.csv`, and `order_items.csv`. These represent the current OLTP structure.
- Your job is to design a star schema (one fact table + at least three dimension tables), create those tables in the SQLite database, and migrate the sample rows into them.
- There is no single correct answer here - different reasonable designs are expected. What matters is that your fact table is at the right grain and your dimensions are cleanly separated.
- Reading the CSVs only needs `read_csv` from the Pandas Fundamentals module. Looping through rows to migrate them isn't covered there directly - `.iterrows()` is the common way to do it, or you can loop with `range(len(df))` and `.iloc[i]`, which uses only what that module already covers. Either is fine here.
