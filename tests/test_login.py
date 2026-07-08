"""
test_login.py
Unit tests for login and validation
"""

import unittest
from utils.validator import (
    validate_username,
    validate_email,
    validate_password,
    validate_registration
)


class TestLoginValidation(unittest.TestCase):

    # -----------------------------
    # Username Tests
    # -----------------------------

    def test_valid_username(self):
        valid, _ = validate_username("yasmeen123")
        self.assertTrue(valid)

    def test_short_username(self):
        valid, _ = validate_username("ab")
        self.assertFalse(valid)

    def test_invalid_username(self):
        valid, _ = validate_username("user@123")
        self.assertFalse(valid)

    # -----------------------------
    # Email Tests
    # -----------------------------

    def test_valid_email(self):
        valid, _ = validate_email("student@example.com")
        self.assertTrue(valid)

    def test_invalid_email(self):
        valid, _ = validate_email("student.com")
        self.assertFalse(valid)

    # -----------------------------
    # Password Tests
    # -----------------------------

    def test_valid_password(self):
        valid, _ = validate_password("Password123")
        self.assertTrue(valid)

    def test_short_password(self):
        valid, _ = validate_password("Pass1")
        self.assertFalse(valid)

    def test_password_without_uppercase(self):
        valid, _ = validate_password("password123")
        self.assertFalse(valid)

    def test_password_without_number(self):
        valid, _ = validate_password("Password")
        self.assertFalse(valid)

    # -----------------------------
    # Registration Test
    # -----------------------------

    def test_valid_registration(self):

        valid, _ = validate_registration(
            "Yasmeen Begum",
            "yasmeen123",
            "yasmeen@example.com",
            "Password123"
        )

        self.assertTrue(valid)


if __name__ == "__main__":
    unittest.main()