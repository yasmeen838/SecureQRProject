from flask import Blueprint, render_template, request, session
from models.message import Message
from encryption.decrypt import decrypt_message

view_bp = Blueprint("view", __name__)


@view_bp.route("/view/<int:message_id>", methods=["GET", "POST"])
def view_message(message_id):

    message = Message.query.get_or_404(message_id)

    decrypted_message = None
    error = None

    # Show the message if it is already stored in the session
    if session.get(f"message_{message_id}"):
        decrypted_message = session.get(f"message_{message_id}")

    if request.method == "POST":

        secret_key = request.form.get("secret_key")

        result = decrypt_message(
            message.encrypted_message,
            secret_key
        )

        if result.startswith("❌"):
            error = result
        else:
            session[f"message_{message_id}"] = result
            decrypted_message = result

    return render_template(
        "view_message.html",
        decrypted_message=decrypted_message,
        error=error
    )