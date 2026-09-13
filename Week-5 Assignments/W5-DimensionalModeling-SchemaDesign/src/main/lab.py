import pandas as pd
import sqlite3

def build_star_schema():

    # Loading the four normalized OLTP source tables into pandas DataFrames
    customers = pd.read_csv(r"src/data/customers.csv", sep="\t", encoding="utf-8")
    products = pd.read_csv(r"src/data/products.csv", sep="\t", encoding="utf-8")
    orders = pd.read_csv(r"src/data/orders.csv", sep="\t", encoding="utf-8")
    order_items = pd.read_csv(r"src/data/order_items.csv", sep="\t", encoding="utf-8")

    # Setting up a connection to SQLite database
    conn = sqlite3.connect("src/data/star_schema.db")
    cursor = conn.cursor()

    # TO DO: Decide your grain
    # Your task: In a comment here, state what one row in your fact table represents
    # (e.g. one row per order line item, not one row per order).

    # TO DO: Create the fact table
    # Your task: Write a CREATE TABLE statement for your fact table.
    # It should hold foreign keys to your dimension tables plus measurable values
    # (e.g. quantity, revenue). Think carefully about what belongs here vs. in a dimension.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fact_Sales (
        -- fill in your columns here
    )
    """)

    # TO DO: Create the dimension tables
    # Your task: Write CREATE TABLE statements for at least three dimension tables
    # (for example Dim_Customer, Dim_Product, Dim_Date) that hold the descriptive
    # context around the fact.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dim_Customer (
        -- fill in your columns here
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dim_Product (
        -- fill in your columns here
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dim_Date (
        -- fill in your columns here
    )
    """)

    # TO DO: Populate the dimension tables
    # Your task: Insert distinct customer, product, and date values from the source
    # DataFrames into your new dimension tables.

    # TO DO: Populate the fact table
    # Your task: Join orders + order_items + products to build fact rows, look up
    # the correct dimension keys, and insert the resulting rows into Fact_Sales.

    # TO DO: Verify your design
    # Your task: Write a SELECT query that joins your fact table back to all three
    # dimension tables and prints a few readable rows (e.g. customer name, product
    # name, order date, quantity) to confirm the design actually works end to end.
    cursor.execute("""  SELECT 1;  """)

    conn.commit()
    conn.close()
    print("\n✅ Star Schema Build Completed!")

if __name__ == "__main__":
    build_star_schema()
