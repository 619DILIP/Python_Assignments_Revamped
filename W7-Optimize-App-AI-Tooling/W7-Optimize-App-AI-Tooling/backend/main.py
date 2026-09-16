from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection, init_db
import os

app = FastAPI(title="Inventory Dashboard - Phase 2 (Reference Build)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "inventory.db")):
        init_db()


@app.get("/api/items")
def get_items():
    conn = get_connection()
    rows = conn.execute("SELECT id, name, category, quantity, unit_cost FROM items").fetchall()
    conn.close()
    return [dict(row) for row in rows]


# This endpoint is deliberately inefficient. It pulls every row into memory
# once (fine), then for each category re-scans that entire in-memory list in
# a Python loop to find matches and total them up, instead of either
# filtering in SQL or doing a single pass that buckets every row by category.
# With 8 categories and a large item count, that's 8 full passes over the
# whole dataset done in the Python interpreter, which is a lot slower than
# either the database or a single grouping pass would be. Everything else in
# this build is the already-fixed reference version; this is the one thing
# you're optimizing.
@app.get("/api/summary")
def get_summary():
    conn = get_connection()
    all_items = conn.execute("SELECT category, quantity, unit_cost FROM items").fetchall()
    conn.close()

    categories = []
    for row in all_items:
        c = row["category"]
        found = False
        for existing in categories:
            if existing == c:
                found = True
        if not found:
            categories.append(c)

    result = []
    for category in categories:
        total = 0.0
        count = 0
        for row in all_items:
            if row["category"] == category:
                total += row["quantity"] * row["unit_cost"]
                count += 1
        result.append({"category": category, "item_count": count, "total_value": round(total, 2)})

    return result


@app.get("/api/low-stock")
def get_low_stock():
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name, category, quantity, unit_cost FROM items WHERE quantity < 50"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
