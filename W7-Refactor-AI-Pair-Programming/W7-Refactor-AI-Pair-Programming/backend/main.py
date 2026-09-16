from fastapi import FastAPI
from database import get_connection, init_db
import os

app = FastAPI(title="Inventory Dashboard - Phase 1")

# NOTE: no CORS middleware is configured here. The frontend runs on its own
# port (see the frontend README section), so without it the browser will
# block every request from the frontend to this API.


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


@app.get("/api/summary")
def get_summary():
    conn = get_connection()
    d = conn.execute("SELECT category FROM items").fetchall()
    cats = []
    for row in d:
        c = row["category"]
        found = False
        for existing in cats:
            if existing == c:
                found = True
        if not found:
            cats.append(c)

    result = []
    for c in cats:
        rows = conn.execute("SELECT quantity, unit_cost FROM items WHERE category = ?", (c,)).fetchall()
        total = 0
        count = 0
        for row in rows:
            total = total + (row["quantity"] * row["unit_cost"])
            count = count + 1
        result.append({"category": c, "item_count": count, "total_value": round(total, 2)})
    conn.close()
    return result


@app.get("/api/low-stock")
def get_low_stock():
    conn = get_connection()
    rows = conn.execute("SELECT id, name, category, quantity, unit_cost FROM items").fetchall()
    conn.close()
    low = []
    for row in rows:
        if row["unit_cost"] < 50:
            low.append(dict(row))
    return low
