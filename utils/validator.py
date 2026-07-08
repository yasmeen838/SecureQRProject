"""
validator.py
Validation utilities for Secure QR Code System
"""

import re

# Allowed image extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def validate_username(username):
    """
    Username must be 3-20 characters and contain only
    letters, numbers, and underscores.
    """

    if not username:
        return False, "Username is required."

    username = username.strip()

    if len(username) < 3 or len(username) > 20:
        return False, "Username must be between 3 and 20 characters."

    if not re.match(r"^[A-Za-z0-9_]+$", username):
        return False, "Username can contain only letters, numbers, and underscores."

    return True, ""


def validate_email(email):
    """
    Validate email format.
    """

    if not email:
        return False, "Email is required."

    email = email.strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(pattern, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password):
    """
    Password must contain:
    - Minimum 8 characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    """

    if not password:
        return False, "Password is required."

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    return True, ""


def validate_message(message):
    """
    Validate QR message.
    """

    if not message:
        return False, "Message cannot be empty."

    message = message.strip()

    if len(message) == 0:
        return False, "Message cannot be blank."

    if len(message) > 1000:
        return False, "Message cannot exceed 1000 characters."

    return True, ""


def allowed_file(filename):
    """
    Validate uploaded image extension.
    """

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def sanitize_input(text):
    """
    Remove leading/trailing whitespace.
    """

    if text is None:
        return ""

    return text.strip()


def validate_qr_image(file):
    """
    Validate uploaded QR image.
    """

    if file is None:
        return False, "No file uploaded."

    if file.filename == "":
        return False, "Please choose an image."

    if not allowed_file(file.filename):
        return False, "Only PNG, JPG, and JPEG files are allowed."

    return True, ""


def validate_registration(full_name, username, email, password):
    """
    Validate all registration fields together.
    """

    if not full_name or len(full_name.strip()) < 3:
        return False, "Full name must contain at least 3 characters."

    valid, msg = validate_username(username)
    if not valid:
        return valid, msg

    valid, msg = validate_email(email)
    if not valid:
        return valid, msg

    valid, msg = validate_password(password)
    if not valid:
        return valid, msg

    return True, "Validation successful."