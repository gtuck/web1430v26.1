# Week 13 Lecture Notes: Component Communication, Reactive Forms, and Derived State

## Weekly focus
Making components talk to each other: passing data down with props, sending events up with `defineEmits`, and managing form state with `v-model`.

## Why this matters
A component that cannot communicate with other components is an island. Real applications are networks of components that share state and respond to each other's actions. Understanding the props-down/events-up pattern is the mental model that transfers directly to React (props + callbacks), Svelte (props + dispatched events), and every other component framework you will encounter. Getting this pattern right also keeps components testable and reusable.

## Learning targets
- Use `defineEmits` in a child component to declare and emit a named event to a parent
- Apply the props-down/events-up pattern to move data up the component tree
- Bind form inputs with `v-model` and explain how it differs from manually wiring `:value` and `@input`
- Use `computed()` to derive state (filtered list, running total, character count) from a `ref`
- Distinguish when to use `reactive()` vs `ref()` for managing a group of related form fields
- Use `nextTick` to defer DOM-dependent logic until after Vue has finished updating the DOM

## Core concepts

### Props down, events up
This is the fundamental data-flow rule in Vue (and most component frameworks). A parent owns the data. It passes slices of that data down to children via props. When a child needs to change something, it does not mutate the prop — it emits an event and lets the parent decide what to do.

Why not just mutate the prop? Because the parent owns that data. If a child mutates a prop directly, the parent's state and the child's rendered state can drift apart silently. Emitting an event keeps the parent in control and makes data flow easy to trace.

### defineEmits
`defineEmits` declares the events a component is allowed to emit. It returns an `emit` function:

```vue
<!-- components/FilterBar.vue -->
<script setup>
defineProps({
  modelValue: String
})

const emit = defineEmits(['update:modelValue', 'clear'])

function handleInput(event) {
  emit('update:modelValue', event.target.value)
}

function handleClear() {
  emit('clear')
}
</script>

<template>
  <div class="filter-bar">
    <input :value="modelValue" @input="handleInput" placeholder="Search..." />
    <button @click="handleClear">Clear</button>
  </div>
</template>
```

In the parent:

```vue
<FilterBar v-model="searchQuery" @clear="searchQuery = ''" />
```

### v-model on a component
When you write `v-model="searchQuery"` on a native `<input>`, Vue automatically binds `:value` and `@input`. When you write `v-model` on a *component*, Vue expands it to `:modelValue="searchQuery"` and `@update:modelValue="searchQuery = $event"`.

That is why the child declares a `modelValue` prop and emits `update:modelValue`. This is a Vue convention, not magic. You can support multiple v-models on the same component by naming them: `v-model:title="post.title"` expands to `:title` and `@update:title`.

### computed() for derived state
`computed()` is the right tool whenever a value should automatically stay in sync with other reactive state. Common examples: a filtered list, a character count, a formatted price, a form validity flag.

```vue
<script setup>
import { ref, computed } from 'vue'

const searchQuery = ref('')
const items = ref([
  { id: 1, name: 'Alpine Trail Map' },
  { id: 2, name: 'Waterproof Jacket' },
  { id: 3, name: 'Trail Runners' }
])

const filteredItems = computed(() =>
  items.value.filter(item =>
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
)
</script>

<template>
  <input v-model="searchQuery" placeholder="Filter items..." />
  <p>{{ filteredItems.length }} result(s)</p>
  <ul>
    <li v-for="item in filteredItems" :key="item.id">{{ item.name }}</li>
  </ul>
</template>
```

The filtered list recalculates whenever `searchQuery` or `items` changes. You do not call it — you just reference `filteredItems` in the template.

### reactive() vs ref() for forms
`ref()` wraps a single value. `reactive()` wraps an object and makes every property reactive without `.value` access:

```js
import { reactive } from 'vue'

const form = reactive({
  name: '',
  email: '',
  role: 'viewer'
})
```

In the template: `v-model="form.name"`, `v-model="form.email"`. No `.value` needed on `reactive()` properties.

When to use which:
- `ref()` — single values, primitives, arrays you want to replace entirely
- `reactive()` — grouped form fields or any object where you always access it as a whole

Caution: you cannot destructure a `reactive()` object and keep reactivity. `const { name } = form` creates a plain string. Use `toRefs(form)` if you need to destructure.

### Handling form submission
A common form pattern with validation:

```vue
<script setup>
import { reactive, ref, computed } from 'vue'

const form = reactive({ name: '', email: '' })
const submitted = ref(false)

const isValid = computed(() =>
  form.name.trim() !== '' && form.email.includes('@')
)

function handleSubmit() {
  if (!isValid.value) return
  submitted.value = true
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <label for="name">Name</label>
    <input id="name" v-model="form.name" />

    <label for="email">Email</label>
    <input id="email" type="email" v-model="form.email" />

    <button type="submit" :disabled="!isValid">Submit</button>
  </form>
  <p v-if="submitted">Thank you, {{ form.name }}!</p>
</template>
```

`@submit.prevent` calls `event.preventDefault()` before your handler runs, so the browser does not perform a full page reload.

### nextTick for focus management
After you change reactive state, Vue batches DOM updates and applies them asynchronously. If you need to interact with the DOM immediately after a state change — for example, focusing a newly revealed input — you must wait for Vue's update cycle to complete:

```js
import { ref, nextTick } from 'vue'

const showInput = ref(false)
const inputRef = ref(null)

async function revealAndFocus() {
  showInput.value = true
  await nextTick()
  inputRef.value?.focus()
}
```

In the template: `<input v-if="showInput" ref="inputRef" />`. Without `nextTick`, `inputRef.value` is `null` because the DOM element has not been created yet.

### Keeping components focused (single responsibility)
A component that does too much becomes hard to debug and impossible to reuse. A practical rule: if you cannot describe what a component does in one short sentence without using "and", consider splitting it.

- `SearchBar.vue` — renders an input, emits the query string
- `ItemList.vue` — receives an array of items, renders them
- `ItemCard.vue` — receives a single item, renders it

`App.vue` (or a page-level component) owns the data array and the query string, passes them down, and wires up the events. This is the single responsibility principle applied to UI components.

## Common mistakes

1. **Mutating a prop directly.** `props.items.push(...)` inside a child component will appear to work but breaks the data-flow contract and causes Vue to emit a warning. Emit an event and let the parent modify its own state.

2. **Forgetting `@submit.prevent` on a form.** Without `prevent`, a form submission causes a full page reload. In a Vite dev server you will see the page flash; in production the user loses all state.

3. **Destructuring `reactive()` and losing reactivity.** `const { name } = reactive({ name: '' })` gives you a plain string that is no longer tracked. Use `v-model="form.name"` directly, or use `toRefs`.

4. **Putting a side effect inside `computed()`.** Computed properties must be pure — no `fetch()`, no `localStorage.setItem()`, no `emit()` inside a computed getter. Use `watch()` or `watchEffect()` for side effects.

5. **Skipping `nextTick` when programmatically focusing an element.** The DOM is not updated synchronously after reactive state changes. Always await `nextTick()` before querying or manipulating a DOM element that depends on that state change.

## Accessibility connection
Form labels are not optional. Every `<input>` needs an associated `<label>` — either wrapping the input or connected via matching `for` and `id` attributes. `v-model` handles the binding of data but does nothing for label association. When you disable a submit button with `:disabled="!isValid"`, some screen readers will not announce why the button is disabled; consider adding a visible or visually-hidden explanation near the form. Focus management with `nextTick` is not just a convenience — it is essential for users navigating a multi-step form by keyboard, because they need focus to land in the right place after each step transition.

## Demo walkthrough
1. Start from the card project built in Week 12.
2. Add a `SearchBar.vue` component with a single text `<input>`. Wire it as a controlled component: accept `modelValue` as a prop and emit `update:modelValue` on input so the parent can use `v-model` on it.
3. In `App.vue`, add `const searchQuery = ref('')` and bind `v-model="searchQuery"` to `SearchBar`.
4. Add a `computed()` that filters the cards array using `searchQuery`. Replace `v-for="card in cards"` with `v-for="card in filteredCards"`.
5. Show in Vue DevTools that `filteredCards` updates live as you type.
6. Add a "Delete" button inside `CardItem.vue`. Use `defineEmits(['delete'])` and emit the card's `id`. In the parent, handle `@delete` and splice the item from the array.
7. Add a small form (two fields, submit button) that pushes a new card object onto `cards`. Use `reactive()` for the form fields. Show the computed list reactively includes the new item after submission and the filtered list updates immediately.

## Practice prompt
Build a `CommentForm.vue` component with `reactive()` fields for `author` and `body`. Use a `computed()` to determine form validity (both fields non-empty, body at least 10 characters). Display a live character count below the body field derived from `form.body.length`. Emit a `submit` event to the parent with the form data when the user submits. In the parent, push each submitted comment onto an array and render the list below the form.

## Bridge
Lab 12 — Small Data Dashboard has you build a filterable, sortable list with components communicating through props and events — the exact pattern from today's demo. Assignment 6 asks you to document the data flow of your Project 2 components: identify what each component owns, what it receives as props, and what events it emits. Drawing that diagram before you write the code will save significant debugging time.
