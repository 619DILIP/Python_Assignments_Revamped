import sqlite3
import os
import random

DB_PATH = os.path.join(os.path.dirname(__file__), "inventory.db")

CATEGORIES = ["Electronics", "Office Supplies", "Furniture", "Kitchen", "Tools", "Outdoor", "Stationery", "Storage"]
NAME_STEMS = ["Widget", "Component", "Unit", "Kit", "Set", "Pack", "Module", "Device", "Accessory", "Bundle"]

random.seed(7)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(n_items=30000):
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_cost REAL NOT NULL
        )
        """
    )
    rows = []
    for i in range(n_items):
        cat = random.choice(CATEGORIES)
        stem = random.choice(NAME_STEMS)
        name = f"{cat} {stem} #{i + 1}"
        qty = random.randint(0, 500)
        cost = round(random.uniform(2.0, 300.0), 2)
        rows.append((name, cat, qty, cost))
    conn.executemany(
        "INSERT INTO items (name, category, quantity, unit_cost) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database seeded.")
