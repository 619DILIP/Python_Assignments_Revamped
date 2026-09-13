# 🏆 ETL Data Pipeline Assignment

## Overview

This assignment is designed to help you build a simple ETL pipeline that extracts messy transaction data, cleans it, and loads it into a usable output.

## Instructions

1. Clone the repository to your local system.

2. Open the project in VS Code.

3. Implement your code inside `src/main/lab.py`.

4. Run your script and check the output.

5. Take a screenshot of your output, add it to the assignment folder, and compress the whole folder into a zip file for submission. If you created a virtual environment (`.venv`) while working on this, remove it before zipping as it's large and not needed for grading.

## Notes

- The `raw_sales_export.csv` dataset is provided inside the `src/data/` folder. It intentionally has real-world mess: missing quantities, missing total prices, inconsistent date formats, and a duplicate row.
- The code should extract the CSV, clean it according to the rules in `lab.py`, log what got skipped and why, and write the cleaned result to a new CSV.

Good luck! 🚀
