import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret Key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "secure_qr_project_secret_key"
    )

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "secure_qr.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Folders
    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads",
        "scanned_qr"
    )

    QR_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "generated_qr"
    )

    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg"
    }

    KEY_FILE = os.path.join(
        BASE_DIR,
        "encryption",
        "secret.key"
    )

    # Change this after deployment
    BASE_URL = os.environ.get(
        "BASE_URL",
        "http://127.0.0.1:5000"
    )