from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt
from app.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(users_bp)

    return app