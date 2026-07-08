"""
test_qr.py
Unit tests for QR code generation and decoding
"""

import os
import unittest

from qr.generate_qr import generate_qr
from qr.decode_qr import decode_qr


class TestQRCode(unittest.TestCase):

    def setUp(self):
        self.test_message = "Secure QR Code Test"
        self.output_dir = "static/generated_qr"
        self.output_file = os.path.join(self.output_dir, "test_qr.png")

        # Create directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def tearDown(self):
        # Remove test QR image after each test
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    # ---------------------------------------
    # QR Generation Tests
    # ---------------------------------------

    def test_generate_qr(self):
        """
        Verify QR image is generated successfully.
        """

        qr_path = generate_qr(self.test_message, self.output_file)

        self.assertTrue(os.path.exists(qr_path))

    def test_generated_file_extension(self):
        """
        Verify generated file is PNG.
        """

        qr_path = generate_qr(self.test_message, self.output_file)

        self.assertTrue(qr_path.endswith(".png"))

    # ---------------------------------------
    # QR Decode Tests
    # ---------------------------------------

    def test_generate_and_decode(self):
        """
        Generate a QR code and decode it.
        """

        qr_path = generate_qr(self.test_message, self.output_file)

        decoded = decode_qr(qr_path)

        self.assertEqual(decoded, self.test_message)

    def test_qr_file_exists(self):
        """
        Ensure generated QR image exists.
        """

        generate_qr(self.test_message, self.output_file)

        self.assertTrue(os.path.isfile(self.output_file))


if __name__ == "__main__":
    unittest.main()