# Week 05 Lecture Notes: Collections, Objects, Methods, and JSON Thinking

## Weekly focus

Modeling information as arrays and objects before writing any DOM or display code.

## Why this matters

Real web applications are data-driven: a product catalog, a to-do list, a user profile — all of it starts as structured data before any HTML is created. Learning to think about data shape first prevents the most common beginner mistake: writing display code and data code tangled together. When you separate the two, you can change what the page looks like without touching the underlying data, and vice versa.

## Learning targets

- Create arrays and objects using literal syntax and access their values correctly
- Use `.map()`, `.filter()`, `.find()`, and `.forEach()` to transform or search array data without writing manual loops
- Read and write object properties using dot notation and bracket notation
- Destructure values from objects and arrays into named variables
- Serialize data to a JSON string with `JSON.stringify` and parse it back with `JSON.parse`
- Describe the "data first" approach: sketch the data shape before writing DOM code

## Core concepts

### Arrays: literals, index access, and length

An array is an ordered list. Items are accessed by zero-based index. The `.length` property always equals the index of the last item plus one.

```js
const colors = ["red", "green", "blue"];

console.log(colors[0]);      // "red"
console.log(colors[2]);      // "blue"
console.log(colors.length);  // 3
console.log(colors[10]);     // undefined — no error, just undefined
```

### Array methods: map, filter, find, forEach

These four methods are the workhorses of data transformation in modern JavaScript. They all accept a callback function that runs once per item.

`.map()` returns a new array of the same length, with each item transformed:

```js
const prices = [10, 20, 30];
const withTax = prices.map(p => p * 1.07);
console.log(withTax); // [10.7, 21.4, 32.1]
```

`.filter()` returns a new array containing only the items that pass a test:

```js
const products = [
  { name: "Shirt", inStock: true },
  { name: "Hat", inStock: false },
  { name: "Shoes", inStock: true },
];
const available = products.filter(p => p.inStock);
// available has 2 items: Shirt and Shoes
```

`.find()` returns the first matching item (or `undefined` if none match):

```js
const found = products.find(p => p.name === "Hat");
console.log(found); // { name: "Hat", inStock: false }
```

`.forEach()` runs a function for each item but does not return a new array — use it for side effects like logging or updating the DOM:

```js
products.forEach(p => {
  console.log(`${p.name}: ${p.inStock ? "available" : "out of stock"}`);
});
```

### Object literals, dot notation, and bracket notation

An object stores key-value pairs. Use dot notation for known, fixed keys. Use bracket notation when the key is dynamic (stored in a variable or contains special characters).

```js
const product = {
  name: "Trail Running Shoes",
  price: 89.99,
  inStock: true,
};

console.log(product.name);           // "Trail Running Shoes"
console.log(product["price"]);       // 89.99

const key = "inStock";
console.log(product[key]);           // true — bracket notation with a variable
```

You can add, update, or delete properties on any object (unless it is frozen):

```js
product.rating = 4.5;        // add
product.price = 79.99;       // update
delete product.inStock;      // remove
```

### Destructuring

Destructuring unpacks values from an object or array into named variables in a single statement — cleaner than writing three separate assignments.

```js
const { name, price } = product;
console.log(name);  // "Trail Running Shoes"
console.log(price); // 79.99

// Array destructuring
const [first, second] = colors;
console.log(first);  // "red"
console.log(second); // "green"

// Rename on destructure
const { name: productName } = product;
console.log(productName); // "Trail Running Shoes"
```

Destructuring is especially useful inside callback functions: `products.map(({ name, price }) => ...)` is more readable than `products.map(p => p.name ...)`.

### JSON.stringify and JSON.parse

JSON (JavaScript Object Notation) is the standard format for sending and storing structured data. `JSON.stringify` converts a JavaScript value to a JSON string. `JSON.parse` converts a JSON string back to a JavaScript value.

```js
const cart = [
  { name: "Shirt", qty: 2 },
  { name: "Hat", qty: 1 },
];

const json = JSON.stringify(cart);
console.log(json);
// '[{"name":"Shirt","qty":2},{"name":"Hat","qty":1}]'
console.log(typeof json); // "string"

const restored = JSON.parse(json);
console.log(restored[0].name); // "Shirt"
```

`JSON.stringify` does not preserve functions, `undefined` values, or `Symbol` keys — they are silently dropped. This is important when debugging missing data.

### Thinking about data shape first

Before writing any HTML or DOM code, sketch your data as a JavaScript array of objects. Ask:

- What is the minimum set of properties each item needs?
- Which properties will be displayed? Which are used only for filtering or logic?
- Is there a unique identifier (an `id`) so you can find and update a specific item?

```js
// Data sketch for a product explorer
const products = [
  { id: 1, name: "Trail Shoes", category: "footwear", price: 89.99, inStock: true },
  { id: 2, name: "Running Hat", category: "accessories", price: 19.99, inStock: false },
  { id: 3, name: "Wool Socks", category: "accessories", price: 12.99, inStock: true },
];
```

Once you have the data shape, the display code becomes mechanical: loop over the array, create a card per item, plug in the properties.

## Common mistakes

1. **Mutating the original array with `.map()`.** `.map()` returns a new array — it does not change the original. Assign the result: `const doubled = prices.map(p => p * 2)`, not `prices.map(...)` with the return value thrown away.
2. **Confusing `.find()` and `.filter()`.** `.find()` returns one item (or `undefined`). `.filter()` always returns an array (possibly empty). If you try to call `.map()` on the result of `.find()`, you will get an error.
3. **Accessing a property on `undefined`.** If `.find()` returns `undefined` and you then write `.name` on the result, you get a TypeError. Always check if the result exists before accessing its properties.
4. **Using dot notation with a dynamic key.** `obj.key` always looks for a property literally named `"key"`. If you have a variable called `key`, you must use `obj[key]`.
5. **Editing the JSON string directly instead of the object.** JSON is a serialization format for transport or storage — not a working data structure. Parse it back to an object before modifying it.

## Accessibility connection

Structuring data as arrays of objects — rather than scraping values directly out of the DOM — keeps your accessible markup clean and authoritative. When you build the DOM from a data array, every element is created deliberately: you can ensure that `alt` text, `aria-label` values, and semantic roles are set from the data rather than inferred or forgotten. It also makes it straightforward to regenerate or update the page without inadvertently stripping ARIA attributes that were added by hand.

## Demo walkthrough

**Demo: Product Data Explorer (Data Layer)**

1. Create `demo-05.js` with a `products` array of six objects, each having `id`, `name`, `category`, `price`, and `inStock` properties.
2. Use `.filter()` to create an `inStockProducts` array and log its length.
3. Use `.map()` to create a `priceLabels` array of formatted strings: `"Trail Shoes — $89.99"`.
4. Use `.find()` to locate the product with `id === 3` and log its name.
5. Destructure `name` and `price` from the found product and log both.
6. Use `JSON.stringify(products, null, 2)` and paste the output into a `<pre>` tag to show how the data looks as JSON — the same format a real API would return.
7. Ask students: "If we needed to add a `rating` property, where in this code would we change it? Would we need to touch the display code?" (Answer: no — that is the benefit of data-first design.)

## Practice prompt

Create a `students` array with at least five objects. Each object should have `name`, `grade` (a number 0–100), and `enrolled` (boolean) properties. Then write three things: (1) use `.filter()` to get only enrolled students, (2) use `.map()` to produce an array of strings in the format `"Alice: B"` using a helper function that converts the grade number to a letter, and (3) use `.find()` to locate a student by name. Log all three results to the console.

## Bridge

The data structures you build this week are exactly what Lab 05's Product Data Explorer will render to the page. For Quiz 3, you should be able to trace through a chain like `products.filter(...).map(...)` and predict its output. Your Project 1 Proposal should include a rough data sketch — an array of objects showing what properties your project's main data will have. That sketch will save you significant time when you start building in Week 06.
