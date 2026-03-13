// Lab 03 – Debugging Exercise
// This file contains THREE bugs. Do not rewrite the logic.
// Read the error messages in the Console and fix only what is broken.
// In notes.md, record: the line number, what was wrong, and what the error message said.

const userName = 'Casey';
const userAge = '28';

function buildWelcome(name, age) {
  const numericAge = parseInt(age);
  const nextYear = numericAge + 1
  return `Hi ${name}! You are ${numericAge} years old. Next year you will be ${nextYeer} years old.`;
}

const message = buildWelcome(userName, userAge)
console.log(mesage);

if (userAge == 28) {
  console.log('Age matched with strict equality');
}
