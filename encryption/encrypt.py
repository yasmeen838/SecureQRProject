from cryptography.fernet import Fernet
import base64
import hashlib


def encrypt_message(message, password):
    # Create a key from the password
    key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(message.encode())

    return encrypted_data.decode()