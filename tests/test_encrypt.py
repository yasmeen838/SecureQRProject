"""
test_encrypt.py
Unit tests for encryption and decryption
"""

import unittest

from encryption.encrypt import encrypt_message
from encryption.decrypt import decrypt_message


class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.message = "This is a Secure QR Code Test"

    # -----------------------------
    # Encryption Tests
    # -----------------------------

    def test_encrypt_returns_string(self):
        encrypted = encrypt_message(self.message)

        self.assertIsInstance(encrypted, str)

    def test_encrypted_text_is_different(self):
        encrypted = encrypt_message(self.message)

        self.assertNotEqual(encrypted, self.message)

    # -----------------------------
    # Decryption Tests
    # -----------------------------

    def test_encrypt_then_decrypt(self):
        encrypted = encrypt_message(self.message)

        decrypted = decrypt_message(encrypted)

        self.assertEqual(decrypted, self.message)

    def test_empty_message(self):
        encrypted = encrypt_message("")

        decrypted = decrypt_message(encrypted)

        self.assertEqual(decrypted, "")

    def test_special_characters(self):
        message = "!@#$%^&*() Secure QR 123"

        encrypted = encrypt_message(message)

        decrypted = decrypt_message(encrypted)

        self.assertEqual(decrypted, message)

    def test_multiline_message(self):
        message = """Hello

This is line 2.

Secure QR Project."""

        encrypted = encrypt_message(message)

        decrypted = decrypt_message(encrypted)

        self.assertEqual(decrypted, message)


if __name__ == "__main__":
    unittest.main()