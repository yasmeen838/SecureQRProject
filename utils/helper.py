"""
helper.py
Utility functions for Secure QR Code System
"""

import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename


def generate_unique_filename(filename):
    """
    Generate a unique filename while preserving the extension.
    """

    extension = os.path.splitext(filename)[1]

    unique_name = f"{uuid.uuid4().hex}{extension}"

    return secure_filename(unique_name)


def get_current_datetime():
    """
    Return the current date and time.
    """

    return datetime.now()


def format_datetime(dt):
    """
    Format a datetime object.
    """

    if dt is None:
        return ""

    return dt.strftime("%d-%m-%Y %I:%M %p")


def allowed_file(filename, allowed_extensions):
    """
    Check whether the uploaded file extension is allowed.
    """

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )


def create_directory(path):
    """
    Create a directory if it does not already exist.
    """

    os.makedirs(path, exist_ok=True)


def get_file_size(filepath):
    """
    Return file size in KB.
    """

    if not os.path.exists(filepath):
        return 0

    size = os.path.getsize(filepath)

    return round(size / 1024, 2)


def delete_file(filepath):
    """
    Delete a file if it exists.
    """

    if os.path.exists(filepath):
        os.remove(filepath)
        return True

    return False


def truncate_text(text, length=40):
    """
    Shorten long text for display.
    """

    if text is None:
        return ""

    if len(text) <= length:
        return text

    return text[:length] + "..."


def calculate_statistics(user, Message, History):
    """
    Calculate dashboard statistics for a user.
    """

    total_messages = Message.query.filter_by(
        user_id=user.id
    ).count()

    total_history = History.query.filter_by(
        user_id=user.id
    ).count()

    return {
        "total_messages": total_messages,
        "total_history": total_history
    }


def application_info():
    """
    Basic application information.
    """

    return {
        "project_name": "Secure QR Code System",
        "version": "1.0",
        "developer": "MCA Final Year Student",
        "year": "2026"
    }