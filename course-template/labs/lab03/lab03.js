// Lab 03 – Console Exercises and Small Programs
// Implement each function below. Do not delete the test calls at the bottom.

// ─── Exercise 1: Greeting ─────────────────────────────────────────────────
// Returns "Hello, [name]! Welcome to WEB 1430."
// If name is empty or only whitespace, returns "Hello, stranger!"

function greet(name) {
  // TODO
}

console.log(greet('Jordan'));   // Expected: "Hello, Jordan! Welcome to WEB 1430."
console.log(greet('  '));       // Expected: "Hello, stranger!"
console.log(greet(''));         // Expected: "Hello, stranger!"

// ─── Exercise 2: Celsius to Fahrenheit ───────────────────────────────────
// Formula: (celsius * 9/5) + 32
// Returns a string formatted to one decimal place: "72.5°F"
// Hint: number.toFixed(1) returns a string with one decimal place.

function toFahrenheit(celsius) {
  // TODO
}

console.log(toFahrenheit(0));     // Expected: "32.0°F"
console.log(toFahrenheit(100));   // Expected: "212.0°F"
console.log(toFahrenheit(-40));   // Expected: "-40.0°F"

// ─── Exercise 3: Password strength ───────────────────────────────────────
// Returns "strong" if length >= 12
// Returns "medium" if length is 8–11
// Returns "weak" if length < 8
// Returns "invalid" if password is not a string or is empty

function checkPassword(password) {
  // TODO
}

console.log(checkPassword('abc'));               // Expected: "weak"
console.log(checkPassword('MyPass123'));         // Expected: "medium"
console.log(checkPassword('MyLongP@ssword!'));   // Expected: "strong"
console.log(checkPassword(''));                  // Expected: "invalid"
console.log(checkPassword(12345));               // Expected: "invalid"

// ─── Exercise 4: Initials ─────────────────────────────────────────────────
// Accepts a full name string, returns the initials in uppercase with dots.
// "Jordan Alex Smith" → "J.A.S."
// Handle extra spaces gracefully.
// Hint: .trim().split(' ') — filter out empty strings from double spaces.

function getInitials(fullName) {
  // TODO
}

console.log(getInitials('Jordan Smith'));          // Expected: "J.S."
console.log(getInitials('Maria Elena Vargas'));    // Expected: "M.E.V."
console.log(getInitials('  Sam   Lee  '));         // Expected: "S.L."
