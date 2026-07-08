/* =====================================
   Secure QR Code System
   Main JavaScript
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Secure QR System Loaded");

    // -----------------------------
    // Auto-hide flash messages
    // -----------------------------
    setTimeout(function () {

        const alerts = document.querySelectorAll(".alert");

        alerts.forEach(function (alert) {

            alert.classList.remove("show");

            setTimeout(function () {
                alert.remove();
            }, 500);

        });

    }, 4000);

    // -----------------------------
    // Confirm Delete
    // -----------------------------
    const deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const confirmDelete = confirm(
                "Are you sure you want to delete this record?"
            );

            if (!confirmDelete) {
                event.preventDefault();
            }

        });

    });

    // -----------------------------
    // Simple Form Validation
    // -----------------------------
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const requiredFields = form.querySelectorAll("[required]");

            let valid = true;

            requiredFields.forEach(function (field) {

                if (field.value.trim() === "") {

                    field.style.border = "2px solid red";

                    valid = false;

                } else {

                    field.style.border = "";

                }

            });

            if (!valid) {

                event.preventDefault();

                alert("Please fill all required fields.");

            }

        });

    });

});


// =====================================
// Copy Text Function
// =====================================

function copyText(id) {

    const element = document.getElementById(id);

    if (!element) {

        alert("Nothing to copy.");

        return;

    }

    element.select();
    element.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(element.value);

    alert("Copied to clipboard!");

}


// =====================================
// Preview Uploaded Image
// =====================================

function previewImage(input, imageId) {

    if (input.files && input.files[0]) {

        const reader = new FileReader();

        reader.onload = function (e) {

            document.getElementById(imageId).src = e.target.result;

        };

        reader.readAsDataURL(input.files[0]);

    }

}


// =====================================
// Character Counter
// =====================================

function countCharacters(textareaId, counterId) {

    const textarea = document.getElementById(textareaId);

    const counter = document.getElementById(counterId);

    if (!textarea || !counter) {

        return;

    }

    counter.innerText = textarea.value.length + " characters";

}


// =====================================
// Password Match Checker
// =====================================

function checkPasswords(passwordId, confirmId, messageId) {

    const password = document.getElementById(passwordId).value;

    const confirm = document.getElementById(confirmId).value;

    const message = document.getElementById(messageId);

    if (!message) return;

    if (confirm === "") {

        message.innerHTML = "";

        return;

    }

    if (password === confirm) {

        message.innerHTML = "Passwords Match";

        message.style.color = "green";

    } else {

        message.innerHTML = "Passwords Do Not Match";

        message.style.color = "red";

    }

}