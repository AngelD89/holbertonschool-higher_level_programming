#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_json_data():
    """Read product data from JSON file."""
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except Exception:
        return None


def get_csv_data():
    """Read product data from CSV file."""
    try:
        products = []
        with open("data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": row["id"],
                    "name": row["name"],
                    "category": row["category"],
                    "price": row["price"]
                })
        return products
    except Exception:
        return None


def get_sql_data():
    """Read product data from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            }
            for r in rows
        ]
    except Exception:
        return None


@app.route("/")
def display_products():
    """Display product data based on selected source."""
    source = request.args.get("source", "json")

    if source == "json":
        products = get_json_data()
    elif source == "csv":
        products = get_csv_data()
    elif source == "sql":
        products = get_sql_data()
    else:
        return render_template("product_display.html", error="Wrong source")

    if products is None:
        return render_template("product_display.html", error="Unable to load data")

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
