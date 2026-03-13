# Week 12 Lecture Notes: Props, State, Templates, and Simple Components

## Weekly focus
What a Vue 3 component is and how to build one using the Composition API with `<script setup>`.

## Why this matters
Every major front-end codebase you will encounter — whether it is Vue, React, or Svelte — is organized around the component model. Learning Vue's Composition API teaches you the underlying pattern (encapsulate state, expose a template, scope styles) so that moving to any other framework later requires learning syntax, not new ideas. Starting with Vite means you are already using the same toolchain professional teams use.

## Learning targets
- Describe what a single-file component (SFC) is and identify its three sections: `<template>`, `<script setup>`, and `<style scoped>`
- Create a reactive variable with `ref()` and bind it to the template using `{{ }}` and `:`
- Use `v-if`, `v-for`, and `@click` in a template to conditionally render and respond to user interaction
- Define props with `defineProps` and pass data from a parent component to a child
- Explain how a Vite + Vue project is wired together: `main.js`, `App.vue`, and the `components/` folder

## Core concepts

### What is a component?
A component bundles three things that used to live in separate files: markup (template), behavior (script), and appearance (style). In Vue, these three sections live together in one `.vue` file. The browser never sees the `.vue` file directly — Vite compiles it into JavaScript before anything is served.

```
src/
  main.js          ← mounts the root Vue app onto #app in index.html
  App.vue          ← root component; imports and arranges other components
  components/
    CardItem.vue   ← a reusable child component
    CardList.vue   ← a component that uses CardItem in a loop
```

`main.js` is the entry point. It does one job:

```js
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

### Single-file component anatomy
A minimal `.vue` file has this shape:

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">Clicked {{ count }} times</button>
</template>

<style scoped>
button {
  font-size: 1rem;
  padding: 0.5rem 1rem;
}
</style>
```

Key details:
- `ref(0)` creates a reactive wrapper around the primitive `0`. Inside the script you read and write it as `count.value`. Inside the template Vue unwraps it automatically, so you write `{{ count }}`, not `{{ count.value }}`.
- `<style scoped>` means the CSS only applies to elements in this component. It does not leak to parent or sibling components.
- `@click` is shorthand for `v-on:click`.

### ref() and reactivity
`ref()` is the primary tool for reactive state in `<script setup>`. When `count.value` changes, Vue re-renders only the parts of the template that depend on it. You do not call any update function; the reactivity system handles it.

Use `ref()` for single values: strings, numbers, booleans, and arrays. The `.value` wrapper is the signal to Vue's reactivity system that this variable should be tracked.

```js
const title = ref('My App')
const isVisible = ref(true)
const items = ref(['Apples', 'Bananas', 'Cherries'])
```

### computed()
`computed()` creates a value that is derived from other reactive state. It recalculates automatically when its dependencies change and caches the result between recalculations.

```js
import { ref, computed } from 'vue'

const items = ref(['Apples', 'Bananas', 'Cherries'])
const count = computed(() => items.value.length)
```

In the template: `{{ count }}` — no `.value` needed, same as `ref`.

### Template directives
Vue directives are special attributes that begin with `v-`. The most common ones:

| Directive | Purpose | Shorthand |
|-----------|---------|-----------|
| `v-bind:href` | Bind an attribute to a JS expression | `:href` |
| `v-on:click` | Attach an event listener | `@click` |
| `v-if` | Conditionally render an element | — |
| `v-for` | Render a list | — |
| `v-model` | Two-way bind a form input | — |

A `v-for` loop always needs a `:key` attribute. The key must be unique and stable — use an id, not the loop index, when the list can change:

```vue
<ul>
  <li v-for="item in items" :key="item.id">
    {{ item.name }}
  </li>
</ul>
```

### defineProps: passing data into a child component
Props are how a parent passes data down to a child. In the child component, declare what props it accepts:

```vue
<!-- components/CardItem.vue -->
<script setup>
defineProps({
  title: String,
  description: String,
  imageUrl: String
})
</script>

<template>
  <article class="card">
    <img :src="imageUrl" :alt="title" />
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
  </article>
</template>
```

In the parent, pass values as attributes:

```vue
<CardItem
  title="Alpine Hike"
  description="A 6-mile trail with 2,000 ft elevation gain."
  imageUrl="/images/hike.jpg"
/>
```

Use `:title="someVariable"` (with the colon) when the value comes from a reactive variable rather than a plain string literal.

### A minimal v-for + component example
This pattern appears in nearly every project: a parent holds the data, a child renders one item, a `v-for` in the parent wires them together.

```vue
<!-- App.vue -->
<script setup>
import { ref } from 'vue'
import CardItem from './components/CardItem.vue'

const cards = ref([
  { id: 1, title: 'Card One', description: 'First card text.' },
  { id: 2, title: 'Card Two', description: 'Second card text.' },
  { id: 3, title: 'Card Three', description: 'Third card text.' }
])
</script>

<template>
  <main>
    <CardItem
      v-for="card in cards"
      :key="card.id"
      :title="card.title"
      :description="card.description"
    />
  </main>
</template>
```

## Common mistakes

1. **Writing `count` instead of `count.value` in the script.** `ref()` returns an object. Inside `<script setup>` you must use `.value` to read or write the wrapped value. The template is the only place where Vue auto-unwraps it.

2. **Omitting `:key` on `v-for`.** Vue will render the list, but it will produce a console warning and can cause subtle bugs when the list is reordered or filtered. Always provide a `:key`.

3. **Using `:title="'Card One'"` when they mean `title="Card One"`.** The colon means "evaluate this as JavaScript." `:title="'Card One'"` works (it evaluates the string literal), but `title="Card One"` is simpler and conventional for plain string props.

4. **Editing `dist/` files.** Vite outputs a `dist/` folder when you run `npm run build`. Those files are generated and will be overwritten. All edits belong in `src/`.

5. **Importing a component but forgetting to use it.** In `<script setup>`, imported components are automatically available in the template — you do not need to register them. But the import line still must be present.

## Accessibility connection
The `<style scoped>` feature does not affect the semantic structure of your HTML. A card component that uses a `<div>` for its container is still a `<div>` after scoping. Choose semantic elements — `<article>`, `<section>`, `<h2>` — inside each component, because the compiled output is what assistive technology reads. When using `v-for` to render images, the `:alt` binding must be dynamic so each image gets a meaningful, unique description rather than a repeated empty or placeholder value.

## Demo walkthrough
1. Scaffold a new project: `npm create vite@latest ui-cards -- --template vue`, then `cd ui-cards && npm install && npm run dev`.
2. Open `src/App.vue`. Delete the default content in `<script setup>` and `<template>`.
3. Create `src/components/CardItem.vue` with `defineProps` for `title` and `description`. Add a template that renders them inside an `<article>`.
4. Back in `App.vue`, import `CardItem` and declare a `ref([])` array with three objects.
5. Add `v-for` with `:key` in the template, passing each object's properties as props.
6. Open the browser. Show Vue DevTools: click a component in the tree and inspect its props in the right panel.
7. Add a `ref(true)` called `showCards` and a button that toggles it. Wrap the list in `v-if="showCards"`. Show it disappear and reappear.

## Practice prompt
Create a `TagBadge.vue` component that accepts a `label` prop (String) and a `color` prop (String, default `'blue'`). In `App.vue`, declare an array of five tag objects and render them with `v-for`. Add a button that appends a new tag to the array and confirm that Vue re-renders the list without a page reload.

## Bridge
Lab 11 — Vue UI Card System asks you to build a card display driven by a data array, which is exactly the `v-for` + component pattern from today. Quiz 7 covers `ref()`, `computed()`, `v-for`, and `defineProps`. Project 2 Build begins this week; the card system you build in the lab is a direct starting point for the project's component layer.
