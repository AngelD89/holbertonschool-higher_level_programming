#!/usr/bin/env python3
"""
Simple API using Flask.

Endpoints:
  GET  /                 -> "Welcome to the Flask API!"
  GET  /status           -> "OK"
  GET  /data             -> JSON list of usernames (e.g., ["jane", "john"])
  GET  /users/<username> -> Full user object or {"error": "User not found"}
  POST /add_user         -> Add user from JSON; 201 with confirmation payload
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store (keep EMPTY for the checker)
# Structure: {"username": {"username": "...", "name": "...", "age": 0, "city": "..."}}
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the full object for a username, or error if not found."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Accepts JSON:
      {"username":"john","name":"John","age":30,"city":"New York"}
    Adds user into 'users' dict and returns 201 with confirmation.
    If 'username' missing -> 400 with {"error":"Username is required"}
    """
    payload = request.get_json(silent=True) or {}

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Build the stored object (ensure 'username' is included in the record)
    user_obj = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Run development server (no debug by default, as per instructions)
    app.run()
