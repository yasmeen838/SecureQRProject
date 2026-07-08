from qr.scan_qr import scan_qr
from encryption.decrypt import decrypt_message


def decode_qr(image_path):
    """
    Scan a QR image and decrypt its contents.

    Parameters:
        image_path (str): Path to the QR code image.

    Returns:
        str: Original decrypted message or an error message.
    """

    # Scan QR image
    encrypted_data = scan_qr(image_path)

    # Check for scan errors
    if encrypted_data.startswith("Error"):
        return encrypted_data

    # Decrypt data
    original_message = decrypt_message(encrypted_data)

    return original_message


if __name__ == "__main__":

    image_path = input("Enter QR Image Path:\n")

    message = decode_qr(image_path)

    print("\nOriginal Message:\n")
    print(message)