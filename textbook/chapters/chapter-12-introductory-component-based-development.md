# Chapter 12: Introductory Component-Based Development

Vue makes a specific promise: when your data changes, the interface updates automatically. You no longer manually query elements and set their text — you declare what the template should look like based on data, and Vue handles the rest.

## What this chapter is really about

This chapter introduces Vue 3 as a gentle framework that brings component structure, reactive data, and declarative templates to the skills you have already built. The goal is not to learn "all of Vue" — it is to understand what a component is, how reactivity works, how data flows between components, and how this connects to the vanilla JavaScript patterns you already know.

## Key ideas

**Single File Components (SFCs)** are `.vue` files with three sections:

```vue
<template>
  <!-- HTML with Vue directives -->
  <h1>{{ title }}</h1>
  <button @click="increment">Count: {{ count }}</button>
</template>

<script setup>
import { ref } from 'vue';

const title = 'My Counter';
const count = ref(0);

function increment() {
  count.value++;
}
</script>

<style scoped>
h1 { color: var(--color-brand); }
</style>
```

The `<script setup>` syntax is the modern Composition API approach. Variables and functions declared here are automatically available in the template.

**`ref()`** creates a reactive value. When you change `.value` in the script, Vue updates everywhere that value is used in the template:

```js
const count = ref(0);
count.value++;   // template re-renders automatically
```

**`computed()`** creates a derived value that updates automatically when its dependencies change:

```js
import { ref, computed } from 'vue';

const price = ref(49.99);
const taxRate = ref(0.08);
const total = computed(() => price.value * (1 + taxRate.value));
// total.value updates whenever price or taxRate changes
```

**Template directives**:

| Directive | Purpose | Example |
|-----------|---------|---------|
| `{{ }}` | Render a value as text | `{{ product.name }}` |
| `v-bind:` or `:` | Bind an attribute to a value | `:class="activeClass"` |
| `v-on:` or `@` | Attach an event listener | `@click="handleClick"` |
| `v-if` / `v-else` | Conditionally render an element | `v-if="isLoggedIn"` |
| `v-for` | Render a list | `v-for="item in items"` |
| `v-model` | Two-way bind an input to data | `v-model="searchQuery"` |

**`v-for`** renders a list of elements from an array. Always include `:key` — it helps Vue track which items changed:

```vue
<ul>
  <li v-for="product in products" :key="product.id">
    {{ product.name }} — {{ product.price }}
  </li>
</ul>
```

**Props** pass data from a parent component to a child:

```vue
<!-- ProductCard.vue -->
<script setup>
defineProps({
  name: String,
  price: Number,
  inStock: Boolean,
});
</script>

<template>
  <article class="product-card">
    <h2>{{ name }}</h2>
    <p>{{ price }}</p>
    <button :disabled="!inStock">Buy</button>
  </article>
</template>
```

```vue
<!-- App.vue — using the component -->
<ProductCard name="Keyboard" :price="49.99" :inStock="true" />
```

**Emits** let a child communicate back to its parent:

```vue
<!-- SearchBar.vue -->
<script setup>
const emit = defineEmits(['search']);

function handleSubmit(event) {
  emit('search', event.target.querySelector('input').value);
}
</script>
```

```vue
<!-- App.vue -->
<SearchBar @search="handleSearch" />
```

## Mental model

In vanilla JavaScript, you imperatively update the DOM: "find this element, set its text to this value." In Vue, you declare what the template should look like based on data, and Vue handles the DOM updates. Change the data; the view follows automatically.

A **component** is a self-contained piece of UI: its own template, its own data, its own behavior. You compose complex interfaces from simple components the same way you compose functions from smaller functions.

Data flows **down** (parent to child via props) and events flow **up** (child to parent via emits). This one-way flow makes it easier to trace where data comes from and where changes originate.

## Working habits

- Install the **Vue DevTools** browser extension. It allows you to visually inspect component state, props, and reactivity in the browser (vanilla DevTools cannot do this effectively).
- Keep components focused — one component, one responsibility. If a component's template is longer than 30 lines, consider splitting it.
- Use `ref()` for primitive values (strings, numbers, booleans). Use `reactive()` for objects when you want to avoid `.value` everywhere.
- Do not mutate props. Props flow down from the parent; a child should not change them directly. Emit an event to the parent and let the parent update its own state.
- Use `computed()` for derived values instead of manually recalculating them in event handlers.
- Remember `.value` — inside `<script setup>`, reading or writing a `ref` requires `.value`. In the `<template>`, Vue unwraps it automatically.

## Common mistakes

- **Mutating props directly**: `props.count++` modifies the parent's data from the child. This breaks one-way data flow and causes bugs that are hard to trace. Emit an event instead.
- **Forgetting `.value` in the script**: `count++` instead of `count.value++` silently does nothing because you are incrementing the `ref` wrapper object, not the value inside it.
- **Putting too much logic in the template**: `v-if="user && user.role === 'admin' && permissions.includes('edit')"` is hard to read. Move complex conditions to `computed()` properties.
- **Missing `:key` in `v-for`**: Vue can't efficiently track which items changed, causing rendering bugs when items are added or removed.
- **Treating Vue like vanilla JS**: trying to `querySelector` inside a component to read or modify the DOM defeats the purpose. Bind to reactive data; let Vue manage the DOM.

## Accessibility and UX note

Vue doesn't change your accessibility obligations — semantic HTML, keyboard interaction, and ARIA still matter inside components. Vue gives you powerful tools to manage them dynamically:

```vue
<!-- Dynamically set aria-expanded based on reactive data -->
<button :aria-expanded="isOpen" @click="isOpen = !isOpen">
  Toggle Menu
</button>
```

Reactive data makes it straightforward to keep ARIA attributes synchronized with visible state — use this intentionally. Ensure that dynamically rendered content (via `v-if` or `v-for`) is keyboard-reachable and announced appropriately by assistive technologies.

## Practice prompt

Build a small product browser in Vue:

1. In `App.vue`, declare a reactive array of at least five product objects (each with `id`, `name`, `price`, `category`, `inStock`).
2. Create a `ProductCard.vue` component that accepts these as props and renders a card with the product name, formatted price, category badge, and a "Buy" button that is disabled when `inStock` is false.
3. In `App.vue`, use `v-for` to render a `ProductCard` for each product. Include `:key`.
4. Add a text input bound with `v-model` to a `searchQuery` ref. Add a `computed` property called `filteredProducts` that returns only products whose name includes `searchQuery` (case-insensitive). Render `filteredProducts` in the `v-for`.
5. Verify the filter updates as you type without any manual DOM manipulation.

## Reflection

When you changed a `ref` value in `<script setup>`, what happened in the template and why? What was the difference between `ref()` and `computed()`? When you tried to mutate a prop directly, what happened? Where did `v-model` replace code you would have written manually with `addEventListener` and `.value`?

## Vocabulary

- **component** — a self-contained piece of UI with its own template, data, and behavior
- **Single File Component (SFC)** — a `.vue` file with `<template>`, `<script setup>`, and `<style>` sections
- **Composition API** — Vue 3's approach to component logic using `ref`, `computed`, and `reactive`
- **ref** — a reactive wrapper for a primitive value; access and mutate with `.value` in the script
- **computed** — a reactive derived value that updates automatically when its dependencies change
- **reactive** — a reactive proxy for an object; properties can be accessed and mutated directly
- **v-bind (`:`)** — directive that binds an HTML attribute to a reactive value
- **v-on (`@`)** — directive that attaches an event listener
- **v-if / v-else** — directives for conditional rendering
- **v-for** — directive for rendering a list of elements from an array
- **v-model** — directive for two-way data binding between an input and a reactive value
- **props** — data passed from a parent component to a child component
- **emit** — a mechanism for a child component to communicate events back to its parent
- **reactivity** — the system by which Vue tracks data dependencies and automatically updates the DOM when data changes

## Mini checklist

- I can create a Vue SFC with `<template>`, `<script setup>`, and `<style scoped>` sections.
- I can declare reactive data with `ref()` and update it with `.value` in the script.
- I can use `v-for` with a `:key` binding to render a list from a reactive array.
- I can use `v-if` to conditionally render an element based on reactive data.
- I can create a child component with `defineProps` and use it in a parent component.
- I can use `computed()` to derive a filtered or transformed value from reactive data.
- I can use `v-model` to bind an input to a reactive value without writing a manual event listener.
- I can explain why props should not be mutated directly and what to do instead.
