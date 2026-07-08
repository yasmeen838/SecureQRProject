from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib


def decrypt_message(encrypted_message, password):

    try:
        # Create key from password
        key = base64.urlsafe_b64encode(
            hashlib.sha256(password.encode()).digest()
        )

        cipher = Fernet(key)

        decrypted = cipher.decrypt(
            encrypted_message.encode()
        )

        return decrypted.decode()

    except InvalidToken:
        return "❌ Wrong Secret Key"

    except Exception:
        return "❌ Unable to decrypt message"