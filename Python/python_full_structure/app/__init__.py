from flask import Flask
from .db import db
from .config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app
