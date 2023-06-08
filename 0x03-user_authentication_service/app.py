#!/usr/bin/env python3
"""Flask application."""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index():
    """Welcome route."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Register a new user."""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login():
    """Login a user."""
    email = request.form.get("email")
    password = request.form.get("password")
    if None in (email, password):
        abort(401)
    if AUTH.valid_login(email, password):
        response = jsonify({"email": email, "message": "logged in"})
        session_id = AUTH.create_session(email)
        if session_id is None:
            abort(401)
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Log out a user."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile")
def profile():
    """Get the logged in user's profile."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
