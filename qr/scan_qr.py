import cv2

def scan_qr(image_path):
    """
    Scan a QR code image and return the decoded data.

    Parameters:
        image_path (str): Path to the QR image.

    Returns:
        str: Decoded text from the QR code.
    """

    try:
        # Read image
        image = cv2.imread(image_path)

        if image is None:
            return "Error: Unable to read image."

        # OpenCV QR Code Detector
        detector = cv2.QRCodeDetector()

        data, points, _ = detector.detectAndDecode(image)

        if not data:
            return "Error: No QR Code found."

        return data

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    image_path = input("Enter QR Image Path:\n")

    result = scan_qr(image_path)

    print("\nDecoded Data:\n")
    print(result)