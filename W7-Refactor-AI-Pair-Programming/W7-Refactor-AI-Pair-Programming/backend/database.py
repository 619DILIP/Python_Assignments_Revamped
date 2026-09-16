import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "inventory.db")

CATEGORIES = ["Electronics", "Office Supplies", "Furniture", "Kitchen", "Tools", "Outdoor", "Stationery", "Storage"]

SEED_ITEMS = [
    ("Wireless Mouse", "Electronics", 84, 19.99),
    ("USB-C Hub", "Electronics", 12, 34.50),
    ("Mechanical Keyboard", "Electronics", 41, 79.00),
    ("Monitor Stand", "Electronics", 30, 45.25),
    ("Webcam", "Electronics", None, 55.00),
    ("Desk Lamp", "Furniture", 65, 22.75),
    ("Office Chair", "Furniture", 18, 149.99),
    ("Standing Desk", "Furniture", 9, 299.00),
    ("Bookshelf", "Furniture", 22, 89.50),
    ("Filing Cabinet", "Storage", 15, 120.00),
    ("Storage Bin (Large)", "Storage", 140, 12.99),
    ("Storage Bin (Small)", "Storage", 210, 6.50),
    ("Label Maker", "Office Supplies", 27, 38.20),
    ("Stapler", "Office Supplies", 95, 8.75),
    ("Sticky Notes (Pack)", "Office Supplies", None, 3.25),
    ("Notebook", "Stationery", 300, 2.50),
    ("Pen Set", "Stationery", 180, 5.99),
    ("Whiteboard Markers", "Stationery", 44, 7.20),
    ("Coffee Mug", "Kitchen", 60, 9.99),
    ("Electric Kettle", "Kitchen", 14, 42.00),
    ("Mini Fridge", "Kitchen", 6, 110.00),
    ("Cordless Drill", "Tools", 11, 89.99),
    ("Tool Box", "Tools", 8, 54.50),
    ("Measuring Tape", "Tools", 70, 6.25),
    ("Camping Chair", "Outdoor", 33, 28.00),
    ("Cooler Box", "Outdoor", None, 65.00),
    ("Patio Umbrella", "Outdoor", 5, 78.40),
]


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER,
            unit_cost REAL NOT NULL
        )
        """
    )
    conn.executemany(
        "INSERT INTO items (name, category, quantity, unit_cost) VALUES (?, ?, ?, ?)",
        SEED_ITEMS,
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database seeded.")
