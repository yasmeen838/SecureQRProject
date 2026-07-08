/* =====================================
   Secure QR Code System
   scanner.js
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    const qrInput = document.getElementById("qrImage");
    const preview = document.getElementById("previewImage");
    const fileInfo = document.getElementById("fileInfo");

    if (!qrInput) {
        return;
    }

    qrInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) {
            return;
        }

        // Allowed image types
        const allowedTypes = [
            "image/png",
            "image/jpeg",
            "image/jpg"
        ];

        if (!allowedTypes.includes(file.type)) {

            alert("Please select a PNG or JPG image.");

            qrInput.value = "";

            if (preview) {
                preview.style.display = "none";
            }

            return;
        }

        // Maximum size: 5 MB
        if (file.size > 5 * 1024 * 1024) {

            alert("Image size must be less than 5 MB.");

            qrInput.value = "";

            if (preview) {
                preview.style.display = "none";
            }

            return;
        }

        // Show file information
        if (fileInfo) {

            fileInfo.innerHTML =
                "<strong>File:</strong> " + file.name +
                "<br><strong>Size:</strong> " +
                (file.size / 1024).toFixed(2) + " KB";

        }

        // Preview image
        if (preview) {

            const reader = new FileReader();

            reader.onload = function (e) {

                preview.src = e.target.result;
                preview.style.display = "block";

            };

            reader.readAsDataURL(file);

        }

    });

});


/* =====================================
   Future Webcam QR Scanner
===================================== */

function startWebcamScanner() {

    alert(
        "Webcam QR scanning can be added in a future version using html5-qrcode."
    );

}


/* =====================================
   Reset Scanner Form
===================================== */

function resetScanner() {

    const input = document.getElementById("qrImage");
    const preview = document.getElementById("previewImage");
    const info = document.getElementById("fileInfo");

    if (input) {
        input.value = "";
    }

    if (preview) {
        preview.src = "";
        preview.style.display = "none";
    }

    if (info) {
        info.innerHTML = "";
    }

}