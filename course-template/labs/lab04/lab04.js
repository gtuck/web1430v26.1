// Lab 04 – Trail Recommender and Distance Converter

// ─── Trail data (do not modify) ──────────────────────────────────────────
const trails = [
  { name: 'Lakeside Loop',       distance: 2.5,  hours: 1.5, level: 'beginner' },
  { name: 'Ridgeline Path',      distance: 5,    hours: 3,   level: 'beginner' },
  { name: 'Canyon Crossing',     distance: 8,    hours: 4.5, level: 'intermediate' },
  { name: 'Summit Approach',     distance: 12,   hours: 6,   level: 'intermediate' },
  { name: 'Granite Peak',        distance: 16,   hours: 7,   level: 'advanced' },
  { name: 'Wilderness Circuit',  distance: 20,   hours: 8,   level: 'advanced' },
];

// ─── DOM references ───────────────────────────────────────────────────────
const experienceSelect  = document.getElementById('experience');
const maxDistanceInput  = document.getElementById('max-distance');
const maxHoursInput     = document.getElementById('max-hours');
const findBtn           = document.getElementById('find-btn');
const recommendationDiv = document.getElementById('recommendation');

const incrementInput  = document.getElementById('increment');
const rowCountInput   = document.getElementById('row-count');
const generateBtn     = document.getElementById('generate-btn');
const tableOutputDiv  = document.getElementById('table-output');

// ─── Part 3: Trail recommender functions ─────────────────────────────────

// validateInputs(level, maxDistance, maxHours)
// Returns an error message string if any input is invalid, or null if all valid.
// Rules: level must be 'beginner'|'intermediate'|'advanced'
//        maxDistance must be 1–20
//        maxHours must be 1–8
function validateInputs(level, maxDistance, maxHours) {
  // TODO
}

// findTrail(level, maxDistance, maxHours)
// Returns the first trail matching all three criteria, or null if none match.
function findTrail(level, maxDistance, maxHours) {
  // TODO
}

// renderRecommendation(trail)
// Updates recommendationDiv.
// If trail is null: "No trail matches your criteria. Try adjusting your distance or time."
// If trail found: show name, distance, hours, and difficulty.
// Use createElement + textContent — no innerHTML.
function renderRecommendation(trail) {
  recommendationDiv.innerHTML = ''; // clear previous result
  // TODO
}

// Button handler
findBtn.addEventListener('click', () => {
  // TODO: read values → validate → findTrail → renderRecommendation
});

// ─── Part 4: Distance converter functions ────────────────────────────────

// milesToKm(miles)
// Returns miles converted to kilometers (miles × 1.60934), rounded to 2 decimal places.
function milesToKm(miles) {
  // TODO
}

// renderTable(increment, rows)
// Guard clauses: rows must be 1–20; increment must be >= 0.1
// Builds a <table> with columns Miles | Kilometers using createElement.
// Renders into tableOutputDiv.
function renderTable(increment, rows) {
  tableOutputDiv.innerHTML = ''; // clear previous result
  // TODO
}

generateBtn.addEventListener('click', () => {
  const increment = parseFloat(incrementInput.value);
  const rows      = parseInt(rowCountInput.value, 10);
  renderTable(increment, rows);
});
