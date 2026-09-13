import pandas as pd

def run_pipeline():

    # Extract: loading the raw export into a pandas DataFrame
    file_path = r"src/data/raw_sales_export.csv"
    df = pd.read_csv(file_path, sep="\t", encoding="utf-8")

    rows_read = len(df)
    skipped_rows = []

    # TO DO: Drop rows with missing/non-numeric Quantity
    # Your task: Identify rows where Quantity is missing or can't be read as a
    # number, log the TransactionID of each into skipped_rows with a reason,
    # then drop those rows from df.

    # TO DO: Normalize TransactionDate to YYYY-MM-DD
    # Your task: The dates arrive in more than one format (DD-MM-YYYY, MM/DD/YYYY,
    # and already-correct YYYY-MM-DD). Write logic that detects and converts all
    # of them to a single consistent YYYY-MM-DD format.

    # TO DO: Calculate TotalPrice where missing
    # Your task: Wherever TotalPrice is blank, calculate it as Quantity * UnitPrice
    # and fill it in.

    # TO DO: Remove exact duplicate rows
    # Your task: Identify and drop any rows that are exact duplicates of another
    # row (same CustomerID, Product, Quantity, TransactionDate, etc.).

    # TO DO: Load - write the cleaned result
    # Your task: Write the cleaned DataFrame out to src/data/cleaned_sales_output.csv
    output_path = r"src/data/cleaned_sales_output.csv"
    # df.to_csv(output_path, sep="\t", index=False)

    # TO DO: Print a run summary
    # Your task: Report how many rows were read, how many were skipped (and why,
    # using skipped_rows), and how many rows were written to the output file.
    print(f"Rows read: {rows_read}")
    print(f"Rows skipped: {len(skipped_rows)}")
    for reason in skipped_rows:
        print(f"  - {reason}")

    print("\n✅ Pipeline Run Completed!")

if __name__ == "__main__":
    run_pipeline()
