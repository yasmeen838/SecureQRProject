import os
import time
import qrcode

QR_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "static",
    "generated_qr"
)

os.makedirs(QR_FOLDER, exist_ok=True)


def generate_qr(url):

    filename = f"qr_{int(time.time())}.png"

    filepath = os.path.join(QR_FOLDER, filename)

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(filepath)

    return f"generated_qr/{filename}"