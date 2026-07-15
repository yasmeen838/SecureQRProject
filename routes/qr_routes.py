from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import os
import time

from database import db
from models.message import Message
from encryption.encrypt import encrypt_message
from encryption.decrypt import decrypt_message
from qr.generate_qr import generate_qr
from qr.scan_qr import scan_qr

qr_bp = Blueprint("qr", __name__)

# PythonAnywhere URL
BASE_URL = "https://yasmeen838.pythonanywhere.com"


# ---------------- GENERATE QR ----------------
@qr_bp.route("/generate", methods=["GET", "POST"])
@login_required
def generate():

    qr_image = None

    if request.method == "POST":

        message = request.form.get("message")
        password = request.form.get("password")

        if not message or not password:
            return render_template(
                "generate_qr.html",
                error="Please fill all fields."
            )

        # Encrypt message
        encrypted_text = encrypt_message(message, password)

        # Save to database
        new_message = Message(
            user_id=current_user.id,
            encrypted_message=encrypted_text,
            secret_key=password,
            qr_image=""
        )

        db.session.add(new_message)
        db.session.commit()

        # Public URL (works with Google Lens)
        qr_url = f"{BASE_URL}/view/{new_message.id}"

        # Generate QR Code
        qr_image = generate_qr(qr_url)

        # Save QR image
        new_message.qr_image = qr_image
        db.session.commit()

        return render_template(
            "generate_qr.html",
            qr_image=qr_image,
            qr_url=qr_url,
            success="QR Code Generated Successfully!"
        )

    return render_template("generate_qr.html")


# ---------------- SCAN QR ----------------
@qr_bp.route("/scan", methods=["GET", "POST"])
@login_required
def scan():

    result = None

    if request.method == "POST":

        file = request.files.get("qr_image")
        password = request.form.get("password")

        if not file or not password:
            return render_template(
                "scan.html",
                result="Please upload a QR Code and enter the Secret Key."
            )

        upload_folder = os.path.join("uploads", "scanned_qr")
        os.makedirs(upload_folder, exist_ok=True)

        filename = f"qr_{int(time.time())}.png"
        filepath = os.path.join(upload_folder, filename)

        file.save(filepath)

        scanned_data = scan_qr(filepath)

        if scanned_data.startswith("Error"):
            result = scanned_data
        elif scanned_data.startswith("http"):
            result = f"Open this link in your browser:\n\n{scanned_data}"
        else:
            result = decrypt_message(scanned_data, password)

    return render_template(
        "scan.html",
        result=result
    )


# ---------------- DECRYPT ----------------
@qr_bp.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():

    message = ""

    if request.method == "POST":

        encrypted = request.form.get("encrypted")
        password = request.form.get("password")

        if encrypted and password:
            message = decrypt_message(encrypted, password)
        else:
            message = "Please fill all fields."

    return render_template(
        "decrypt.html",
        message=message
    )


# ---------------- HISTORY ----------------
@qr_bp.route("/history")
@login_required
def history():

    messages = Message.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Message.created_at.desc()
    ).all()

    return render_template(
        "history.html",
        messages=messages
    )