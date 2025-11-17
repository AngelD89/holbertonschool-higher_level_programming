
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ---------- JSON READER ----------
def read_json_file():
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            # Ensure same format as other sources
            if isinstance(data, list):
                return {"products": data}
            return data
    except Exception:
        return None


# ---------- CSV READER ----------
def read_csv_file():
    try:
        products = []
        with open("products.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return {"products": products}
    except Exception:
        return None


# ---------- SQLITE READER ----------
def read_sqlite(id_value=None):
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        if id_value:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (id_value,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })

        return {"products": products}

    except Exception:
        return None


# ---------- ROUTE ----------
@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid id value.")

    if source == "json":
        data = read_json_file()

    elif source == "csv":
        data = read_csv_file()

    elif source == "sql":
        data = read_sqlite(product_id)
    else:
        return render_template("product_display.html", error="Wrong source.")

    if data is None:
        return render_template("product_display.html", error="Error loading data.")

    products = data.get("products", [])

    # If ID provided but not found
    if product_id and len(products) == 0:
        return render_template("product_display.html", error="Product not found.")

    return render_template("product_display.html", products=products)


# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
