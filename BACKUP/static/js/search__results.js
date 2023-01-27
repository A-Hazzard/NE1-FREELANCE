// Get the form and the input elements
const form = $('form');
const usernameInput = $('input[name="search"]');
const passwordInput = $('input[name="password"]');

// Add a submit event listener to the form
form.on('submit', function(event) {
event.preventDefault();

// Get the values of the input elements
const username = usernameInput.val();
const password = passwordInput.val();

// Create a variable to store the validation status
let isValid = true;

// Validate the username
if (username.length < 5) {
alert('Username must be at least 5 characters long.');
isValid = false;
}

// Validate the password
if (password.length < 8) {
alert('Password must be at least 8 characters long.');
isValid = false;
}

if (!/[a-z]/.test(password)) {
alert('Password must contain at least one lowercase letter.');
isValid = false;
}

if (!/[A-Z]/.test(password)) {
alert('Password must contain at least one uppercase letter.');
isValid = false;
}

if (!/[0-9]/.test(password)) {
alert('Password must contain at least one number.');
isValid = false;
}

if (!/[!@#\$%\^&\*]/.test(password)) {
alert('Password must contain at least one symbol.');
isValid = false;
}

// If the input is valid, submit the form
if (isValid) {
form.submit();
}
});
