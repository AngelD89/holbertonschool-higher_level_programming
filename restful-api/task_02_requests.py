#!/usr/bin/python3
"""
Fetch and process data from a REST API (JSONPlaceholder)
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If success, process the data
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure data into list of dictionaries
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)

        print("✅ Data saved successfully to posts.csv")
    else:
        print("Failed to retrieve posts.")
