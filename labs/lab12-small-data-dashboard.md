# Lab 12 – Small Data Dashboard

## Purpose

Reactive forms and derived state are where Vue's reactivity system becomes most visible. This lab builds a data dashboard where user input drives filtered, sorted, and summarized views of a dataset — with no manual DOM manipulation. All updates flow automatically from reactive data changes.

## Skills practiced

- Two-way binding with `v-model`
- Derived data with `computed()`
- Component communication with `defineProps` and `defineEmits`
- Conditional class binding with `:class`
- Rendering summary statistics from computed data
- Passing filter state from parent to child via props

## What you're building

A **Student Grade Dashboard** for a fictional course roster. The dashboard displays:
- A table of students with their name, score, and letter grade
- A search input that filters the table by student name
- A score range filter (min/max)
- A pass/fail toggle (show all / passing only / failing only)
- A summary panel showing count, average, high score, and low score — all derived from the *filtered* dataset

All filtering and aggregation uses `computed()`. The child `SummaryPanel` component receives computed data as props.

---

## Part 1: Scaffold the project

In `labs/`:

```bash
npm create vite@latest lab12 -- --template vue
cd lab12
npm install
```

Clear the default boilerplate. Create:
- `src/components/SummaryPanel.vue`
- `src/components/GradeTable.vue`

Add `node_modules/` and `dist/` to `.gitignore`.

---

## Part 2: Student data

In `src/App.vue` `<script setup>`:

```js
import { ref, computed } from 'vue';
import SummaryPanel from './components/SummaryPanel.vue';
import GradeTable from './components/GradeTable.vue';

const students = ref([
  { id: 1,  name: 'Alex Nguyen',      score: 94 },
  { id: 2,  name: 'Brianna Lee',      score: 72 },
  { id: 3,  name: 'Carlos Herrera',   score: 58 },
  { id: 4,  name: 'Diana Okafor',     score: 88 },
  { id: 5,  name: 'Ethan Park',       score: 45 },
  { id: 6,  name: 'Fatima Al-Rashid', score: 91 },
  { id: 7,  name: 'Grace Kim',        score: 63 },
  { id: 8,  name: 'Hiro Yamamoto',    score: 79 },
  { id: 9,  name: 'Isabelle Martin',  score: 82 },
  { id: 10, name: 'Jordan Smith',     score: 55 },
  { id: 11, name: 'Kira Osei',        score: 97 },
  { id: 12, name: 'Leo Santos',       score: 68 },
]);
```

---

## Part 3: Filter controls (reactive refs)

```js
const searchQuery = ref('');
const minScore = ref(0);
const maxScore = ref(100);
const passFilter = ref('all');   // 'all' | 'passing' | 'failing'
```

---

## Part 4: Computed values

### Letter grade helper

```js
function getGrade(score) {
  if (score >= 90) return 'A';
  if (score >= 80) return 'B';
  if (score >= 70) return 'C';
  if (score >= 60) return 'D';
  return 'F';
}
```

### Filtered students

```js
const filteredStudents = computed(() => {
  return students.value
    .filter(s => s.name.toLowerCase().includes(searchQuery.value.toLowerCase()))
    .filter(s => s.score >= minScore.value && s.score <= maxScore.value)
    .filter(s => {
      if (passFilter.value === 'passing') return s.score >= 60;
      if (passFilter.value === 'failing') return s.score < 60;
      return true;
    })
    .map(s => ({ ...s, grade: getGrade(s.score) }));
});
```

### Summary statistics (derived from filtered data)

```js
const summary = computed(() => {
  const count = filteredStudents.value.length;
  if (count === 0) return { count: 0, average: 'N/A', high: 'N/A', low: 'N/A', passing: 0 };
  const scores = filteredStudents.value.map(s => s.score);
  return {
    count,
    average: (scores.reduce((a, b) => a + b, 0) / count).toFixed(1),
    high: Math.max(...scores),
    low: Math.min(...scores),
    passing: filteredStudents.value.filter(s => s.score >= 60).length,
  };
});
```

---

## Part 5: App.vue template

```vue
<template>
  <div class="dashboard">
    <h1>Grade Dashboard</h1>

    <section class="filters" aria-label="Filter controls">
      <div class="filter-group">
        <label for="search">Search by name</label>
        <input id="search" type="search" v-model="searchQuery" placeholder="Student name…">
      </div>

      <div class="filter-group">
        <label for="min-score">Min score</label>
        <input id="min-score" type="number" v-model.number="minScore" min="0" max="100">
      </div>

      <div class="filter-group">
        <label for="max-score">Max score</label>
        <input id="max-score" type="number" v-model.number="maxScore" min="0" max="100">
      </div>

      <div class="filter-group">
        <label for="pass-filter">Show</label>
        <select id="pass-filter" v-model="passFilter">
          <option value="all">All students</option>
          <option value="passing">Passing only (≥60)</option>
          <option value="failing">Failing only (&lt;60)</option>
        </select>
      </div>
    </section>

    <SummaryPanel :summary="summary" />
    <GradeTable :students="filteredStudents" />
  </div>
</template>
```

---

## Part 6: SummaryPanel component

`src/components/SummaryPanel.vue` — receives summary data as a prop and displays it:

```vue
<script setup>
defineProps({
  summary: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <section class="summary-panel" aria-label="Summary statistics" aria-live="polite">
    <div class="summary-stat">
      <span class="stat-label">Students shown</span>
      <span class="stat-value">{{ summary.count }}</span>
    </div>
    <div class="summary-stat">
      <span class="stat-label">Average score</span>
      <span class="stat-value">{{ summary.average }}</span>
    </div>
    <div class="summary-stat">
      <span class="stat-label">High score</span>
      <span class="stat-value">{{ summary.high }}</span>
    </div>
    <div class="summary-stat">
      <span class="stat-label">Low score</span>
      <span class="stat-value">{{ summary.low }}</span>
    </div>
    <div class="summary-stat">
      <span class="stat-label">Passing</span>
      <span class="stat-value">{{ summary.passing }}</span>
    </div>
  </section>
</template>
```

---

## Part 7: GradeTable component

`src/components/GradeTable.vue` — renders the filtered student list as a table:

```vue
<script setup>
defineProps({
  students: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <div class="table-wrapper">
    <p v-if="students.length === 0" class="empty-msg">No students match the current filters.</p>

    <table v-else aria-label="Student grades">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Score</th>
          <th scope="col">Grade</th>
          <th scope="col">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="student in students"
          :key="student.id"
          :class="student.score < 60 ? 'row--failing' : 'row--passing'"
        >
          <td>{{ student.name }}</td>
          <td>{{ student.score }}</td>
          <td>{{ student.grade }}</td>
          <td>{{ student.score >= 60 ? 'Passing' : 'Failing' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.row--failing { background-color: #fef2f2; }
.row--passing { background-color: #f0fdf4; }
</style>
```

---

## Testing requirements

- [ ] Typing in the search box immediately filters the table and updates the summary
- [ ] Changing min/max score narrows the shown rows
- [ ] Selecting "Passing only" hides failing students; "Failing only" hides passing students
- [ ] All four filters can be active simultaneously and work together
- [ ] Summary stats reflect the *filtered* data, not the full dataset
- [ ] Empty state message shows when no students match
- [ ] `aria-live="polite"` is on the summary panel

---

## Deliverable

Commit `labs/lab12/` (excluding `node_modules/` and `dist/`). Push and deploy.

Submit to Canvas: live URL, repo URL.

---

## Process reflection (in `labs/lab12/notes.md`)

Answer in 4–6 sentences:
- What is `v-model.number` and why did you need it for the score inputs?
- How does the summary panel stay synchronized with the filtered data without any additional event listeners?
- What happens to the summary if all students are filtered out — how did you handle that edge case?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Computed filtering** | All four filters work via `computed`; no manual DOM updates; all filters combine correctly | Three filters in computed | Two filters; one manual DOM update | No computed filtering |
| **Summary panel** | All five stats correct; derived from filtered data; updates with each filter change | Four stats correct; one not filtered | Stats present but use full dataset | No summary |
| **Component structure** | Two child components with correct `defineProps`; data flows parent → child | Two components; prop type missing | One component extracted | Everything in App.vue |
| **Accessibility** | `aria-live` on summary; table uses `scope`; empty state present | Two of three | One | None |
| **Edge cases** | Empty filter result shows message; summary shows "N/A" when count is 0 | Empty state only | Edge cases attempted but broken or inconsistent | No edge case handling |
| **Reflection** | Specific; all three prompts addressed | Two prompts | Vague | Missing |
