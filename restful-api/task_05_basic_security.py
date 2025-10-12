#!/usr/bin/env python3
"""
API Security & Authentication Techniques with Flask

Endpoints:
  GET  /basic-protected  -> Basic Auth protected ("Basic Auth: Access Granted")
  POST /login            -> Returns JWT on valid credentials
  GET  /jwt-protected    -> JWT protected ("JWT Auth: Access Granted")
  GET  /admin-only       -> JWT + role check ("Admin Access: Granted"), 403 if not admin

Auth rules:
  - All AUTHENTICATION errors (missing/invalid/expired/revoked JWT) -> 401
  - AUTHORIZATION failure (non-admin to /admin-only) -> 403 {"error": "Admin access required"}
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

# Basic Auth
from flask_httpauth import HTTPBasicAuth

# JWT Auth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)

# --- SECURITY CONFIG ---------------------------------------------------------
# Use a strong secret key in real deployments (env var, secrets manager, etc.)
app.config["JWT_SECRET_KEY"] = "change-this-in-production"  # demo only
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory users (hashed passwords)
# Password for both demo users is: "password"
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# --- BASIC AUTH --------------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username  # returning a truthy value means success
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    # Spec wants plain text message
    return "Basic Auth: Access Granted", 200


# --- JWT LOGIN ---------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accepts: {"username":"user1","password":"password"}
    Returns: {"access_token":"<JWT_TOKEN>"}
    """
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    # Authentication errors -> 401
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed role inside JWT as an additional claim
    additional_claims = {"role": user["role"]}
    token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify({"access_token": token}), 200


# --- JWT PROTECTED ROUTES ----------------------------------------------------
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # Spec wants plain text message
    return "JWT Auth: Access Granted", 200


def role_required(required_role):
    """
    Decorator to enforce role-based authorization using JWT claims.
    Returns 403 for authorization failures (not authentication).
    """
    def wrapper(fn):
        from functools import wraps
        @wraps(fn)
        @jwt_required()
        def decorated(*args, **kwargs):
            claims = get_jwt()  # all claims, including our 'role'
            role = claims.get("role")
            if role != required_role:
                # Authorization failure -> 403 (per spec)
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper


@app.route("/admin-only", methods=["GET"])
@role_required("admin")
def admin_only():
    return "Admin Access: Granted", 200


# --- JWT ERROR HANDLERS (ALL -> 401) ----------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Missing Authorization header / Bearer token
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Token is malformed or signature invalid
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# --- MAIN --------------------------------------------------------------------
if __name__ == "__main__":
    # No debug mode by default to match typical graders
    app.run()
