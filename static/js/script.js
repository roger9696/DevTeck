// Add your custom JavaScript code here

// Function to validate form fields
function validateForm() {
    var form = document.getElementById('new-video-form');
    var inputs = form.getElementsByTagName('input');
    var isValid = true;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === '') {
            inputs[i].classList.add('is-invalid');
            isValid = false;
        } else {
            inputs[i].classList.remove('is-invalid');
        }
    }

    return isValid;
}

// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault();
    var isValid = validateForm();

    // Check if form is found
    if (form) {
        form.submit(); // Submit the form
    } else {
        // Show error message or handle invalid form fields
        console.log('Please fill in all required fields.');
    }
}



