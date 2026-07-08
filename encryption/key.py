import os
from cryptography.fernet import Fernet

# Path to save the encryption key
KEY_FILE = os.path.join(os.path.dirname(__file__), "secret.key")


def generate_key():
    """
    Generate a new encryption key and save it.
    This only runs if the key file doesn't already exist.
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

        print("Encryption key generated successfully.")
    else:
        print("Encryption key already exists.")


def load_key():
    """
    Load the existing encryption key.
    """
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


# Generate the key automatically when this file is executed
if __name__ == "__main__":
    generate_key()