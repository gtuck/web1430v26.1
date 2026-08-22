// Lab 07 – Accessible Form Validation

// ─── DOM references ───────────────────────────────────────────────────────
const form          = document.getElementById('registration-form');
const nameInput     = document.getElementById('full-name');
const emailInput    = document.getElementById('email');
const phoneInput    = document.getElementById('phone');
const studentIdInput = document.getElementById('student-id');
const eventSelect   = document.getElementById('event-select');
const confirmation  = document.getElementById('confirmation');
const confirmDetails = document.getElementById('confirmation-details');

// ─── Part 2: Validation functions ────────────────────────────────────────
// Each returns an error string if invalid, or null if valid.

function validateName(value) {
  if (!value.trim()) return 'Full name is required.';
  if (value.trim().length < 2) return 'Name must be at least 2 characters.';
  return null;
}

function validateEmail(value) {
  if (!value.trim()) return 'Email address is required.';
  if (!value.includes('@') || !value.includes('.')) return 'Please enter a valid email address.';
  return null;
}

function validatePhone(value) {
  // Optional — only validate format if a value was entered
  if (!value.trim()) return null;
  const digitsOnly = value.replace(/\D/g, '');
  if (digitsOnly.length < 10) return 'Phone number must have at least 10 digits.';
  return null;
}

function validateStudentId(value) {
  if (!value.trim()) return 'Student ID is required.';
  if (!/^\d{7,9}$/.test(value.trim())) return 'Student ID must be 7–9 digits.';
  return null;
}

function validateEvent(value) {
  if (!value) return 'Please select a workshop.';
  return null;
}

// ─── Part 3: Error display functions ─────────────────────────────────────

function showError(inputEl, message) {
  const errorEl = document.getElementById(`${inputEl.id}-error`);
  errorEl.textContent = message;
  inputEl.setAttribute('aria-invalid', 'true');
  inputEl.classList.add('input-error');
}

function clearError(inputEl) {
  const errorEl = document.getElementById(`${inputEl.id}-error`);
  errorEl.textContent = '';
  inputEl.removeAttribute('aria-invalid');
  inputEl.classList.remove('input-error');
}

// ─── Part 4a: Blur validation (early feedback on name + email) ────────────
// TODO: Add blur listeners for nameInput and emailInput.
// Show the error if invalid, clear it if valid.

// ─── Part 4b: Submit handler ──────────────────────────────────────────────
// TODO: Add a submit listener to `form`.
// 1. event.preventDefault()
// 2. Validate all five required fields
// 3. Show errors on invalid fields; clear errors on valid fields
// 4. If any errors: focus the first invalid field and return
// 5. If all valid: hide the form, show confirmation with a summary, move focus to confirmation
