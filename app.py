from flask import Flask, render_template
from flask_login import LoginManager

from config import Config
from database import init_db, db

# Import Models
from models.user import User, bcrypt
from models.message import Message

# Import Blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.qr_routes import qr_bp
from routes.admin import admin_bp
from routes.view_routes import view_bp


def create_app():

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Bcrypt
    bcrypt.init_app(app)

    # Initialize Database
    init_db(app)

    # Create Database Tables
    with app.app_context():
        db.create_all()

    # Flask Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(qr_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(view_bp)

    # Home Page
    @app.route("/")
    def home():
        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )