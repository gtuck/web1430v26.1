# Chapter 5: Modeling Information in JavaScript

Real applications deal with collections of things: products, users, posts, events. This chapter teaches you how to represent those collections as arrays and objects, and how to work with them using the methods that make JavaScript data manipulation readable and expressive.

## What this chapter is really about

Before you can render a product catalog, filter a search result, or build a preferences panel, you need to model the underlying information. This chapter focuses on arrays (ordered lists of things), objects (records with named properties), and the methods that let you transform, filter, and search that data without writing verbose manual loops. It also introduces JSON — the universal language for exchanging data between client and server.

## Key ideas

**Arrays** are ordered, zero-indexed collections:

```js
const colors = ['red', 'green', 'blue'];
console.log(colors[0]);       // 'red'
console.log(colors.length);   // 3
```

**Objects** are collections of named properties:

```js
const product = {
  name: 'Wireless Keyboard',
  price: 49.99,
  inStock: true,
};

console.log(product.name);         // dot notation
console.log(product['price']);     // bracket notation (useful with dynamic keys)
```

**Arrays of objects** are the most common data structure in real applications — for example, a product catalog, a list of users, or search results:

```js
const products = [
  { id: 1, name: 'Keyboard', price: 49.99, category: 'Electronics' },
  { id: 2, name: 'Notebook', price: 4.99, category: 'Stationery' },
  { id: 3, name: 'Monitor', price: 299.00, category: 'Electronics' },
];
```

**Key array methods** — learn these; they replace most manual loops:

| Method | What it does | Returns |
|--------|-------------|---------|
| `.map(fn)` | Transform every item | New array, same length |
| `.filter(fn)` | Keep items that pass a test | New array, shorter or equal length |
| `.find(fn)` | Find the first matching item | One item or `undefined` |
| `.findIndex(fn)` | Find the index of the first match | Number or `-1` |
| `.forEach(fn)` | Run a function on each item | `undefined` (side effects only) |
| `.some(fn)` | True if any item passes | Boolean |
| `.every(fn)` | True if all items pass | Boolean |

```js
// Get only electronics
const electronics = products.filter(p => p.category === 'Electronics');

// Get just the names
const names = products.map(p => p.name);   // ['Keyboard', 'Notebook', 'Monitor']

// Find a specific item
const keyboard = products.find(p => p.id === 1);
```

**Destructuring** extracts properties from objects and arrays into named variables:

```js
const { name, price } = product;        // object destructuring
const [first, second] = colors;         // array destructuring
```

**JSON** (JavaScript Object Notation) is a text format for structured data. It looks like a JavaScript object literal but has strict rules: all keys must be quoted strings, values must be strings, numbers, booleans, `null`, arrays, or objects (no functions, no `undefined`).

```js
// JavaScript object → JSON string
const json = JSON.stringify(product);

// JSON string → JavaScript object
const parsed = JSON.parse(json);
```

## Mental model

An array is for an ordered list of similar items — a list of products, a list of names, a list of search results. An object is for a single record with named attributes — a single product, a single user, a single event.

Most real data is **an array of objects**: a collection of records. When you receive data from an API, you will almost always be working with an array of objects. Build your mental model around that shape and the key methods (`.map`, `.filter`, `.find`) become your primary tools.

Design your data before writing any rendering code. Ask: what information does this interface need? Then define the shape of the data object that holds it. Writing the data model first makes the rendering code obvious.

## Working habits

- Sketch your data structure before writing code. What does one item look like as a JavaScript object?
- Use `.map()` to transform data into display values (prices, labels, HTML strings).
- Use `.filter()` to reduce a collection based on user input.
- Use `.find()` to locate a single item by ID or another unique property.
- Avoid mutating the original array. `.map()` and `.filter()` return new arrays; use them instead of modifying the source.
- Always wrap `JSON.parse()` in a `try/catch` — invalid JSON throws a `SyntaxError`.

## Common mistakes

- **Using `.forEach()` when you want a return value**. `forEach` returns `undefined`. If you need a new array, use `.map()`.
- **Confusing arrays and objects**: arrays are for ordered lists, objects are for records. `products[0]` is an object. `products` is an array.
- **Forgetting zero-indexing**: the first item is at index `0`, the last is at `array.length - 1`.
- **Mutating the original array** with `.push()`, `.splice()`, or direct index assignment when you should be deriving a new array.
- **Treating JSON as JavaScript**: JSON has no `undefined`, no trailing commas, no functions, no comments. `JSON.stringify(undefined)` returns `undefined` (not a string), silently dropping the value.
- **Not handling `.find()` returning `undefined`**: if no item matches, `.find()` returns `undefined`. Calling `.name` on `undefined` throws a TypeError.

## Accessibility and UX note

Your data model determines what information is available to render. If your data model doesn't include an `alt` text field for images, you have no accessible image description to render. If it doesn't include an `aria-label` for an action, your interface will be unlabeled. Think about accessibility attributes as data — they belong in your data model, not as afterthoughts added to the template.

## Practice prompt

Create an array of at least five objects, each representing a book with `id`, `title`, `author`, `year`, and `genre` properties.

Write four functions:
1. `getBooksAfter(books, year)` — returns all books published after the given year
2. `getTitles(books)` — returns an array of just the title strings
3. `findByTitle(books, title)` — returns the book object with that title, or `undefined`
4. `groupByGenre(books)` — returns an object where each key is a genre and its value is an array of books in that genre

Test all four in the console. Handle the case in `findByTitle` where no book matches.

## Reflection

What did you discover when you called `.find()` with a title that didn't exist? When you used `.map()` vs `.forEach()`, what was different about the return value? How did you represent the grouped data in `groupByGenre`, and what does that structure look like when logged?

## Vocabulary

- **array** — an ordered, zero-indexed list of values
- **object** — a collection of named properties (key-value pairs)
- **property** — a named value in an object
- **method** — a function stored as a property of an object (or a built-in array operation)
- **index** — the numeric position of an item in an array (starts at 0)
- **destructuring** — syntax for extracting properties from objects or items from arrays into variables
- **JSON** — JavaScript Object Notation; a text format for structured data exchange
- **iteration** — processing each item in a collection in turn
- **map** — an array method that returns a new array of transformed items
- **filter** — an array method that returns a new array of items that pass a test
- **key-value pair** — a property name and its associated value in an object

## Mini checklist

- I can create an array of objects and access properties using dot notation.
- I can use `.filter()` to return a subset of an array without mutating the original.
- I can use `.map()` to transform an array into a new array of different values.
- I can use `.find()` and handle the case where it returns `undefined`.
- I can use destructuring to extract object properties into named variables.
- I can use `JSON.stringify()` and `JSON.parse()` and explain where each is needed.
