#!/usr/bin/env python3
"""
Flask app to display product data from JSON, CSV, or SQLite database
based on query parameters.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_json():
    """Load products from products.json file."""
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return None


def load_csv():
    """Load products from products.csv file."""
    products = []
    try:
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    "id": int(row.get("id")),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": float(row.get("price"))
                }
                products.append(product)
        return products
    except Exception:
        return None


def load_sql():
    """Load products from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            products.append(product)
        return products
    except Exception:
        return None


@app.route("/products")
def products():
    """Display product data based on source query parameter."""
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")

    # Handle source selection
    if source == "json":
        data = load_json()
    elif source == "csv":
        data = load_csv()
    elif source == "sql":
        data = load_sql()
    else:
        return render_template("product_display.html",
                               error="Wrong source")

    if data is None:
        return render_template("product_display.html",
                               error="Error reading data")

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID format")

        filtered = []
        for product in data:
            if product.get("id") == product_id:
                filtered.append(product)

        if len(filtered) == 0:
            return render_template("product_display.html",
                                   error="Product not found")

        return render_template("product_display.html",
                               products=filtered)

    # If no ID provided → show all products
    return render_template("product_display.html",
                           products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
