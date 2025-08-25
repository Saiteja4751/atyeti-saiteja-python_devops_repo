from flask import Blueprint, request, jsonify
from ..models.user import User
from ..db import db
from .. import bcrypt
from ..utils.token import create_token
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        token = create_token(user.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"username": user.username, "created_at": user.created_at.isoformat()})
