from flask import Blueprint, render_template, request
from models.message import Message
from encryption.decrypt import decrypt_message

view_bp = Blueprint("view", __name__)

@view_bp.route("/view/<int:message_id>", methods=["GET", "POST"])
def view_message(message_id):

    message = Message.query.get_or_404(message_id)

    if request.method == "POST":

        secret_key = request.form.get("secret_key")

        result = decrypt_message(
            message.encrypted_message,
            secret_key
        )

        return f"""
        <h1>Decrypted Message</h1>
        <h2>{result}</h2>
        """

    return """
    <form method="POST">
        <input type="password" name="secret_key" placeholder="Secret Key">
        <button type="submit">Decrypt</button>
    </form>
    """