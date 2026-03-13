// Lab 10 – Starting point: single-file "bundle"
// This is the monolithic script you will refactor into a Vite module project.
// Do NOT submit this file. Use it as your reference only.
// Your goal: same behavior, reorganized into src/data.js, utils.js, render.js, events.js, main.js

// All code in one file — globals everywhere

const products = [
  { id: 1, name: 'Notebook',      price: 4.99,  category: 'Stationery' },
  { id: 2, name: 'USB Hub',       price: 29.99, category: 'Electronics' },
  { id: 3, name: 'Hoodie',        price: 39.99, category: 'Apparel' },
  { id: 4, name: 'Keyboard',      price: 89.99, category: 'Electronics' },
  { id: 5, name: 'Sticky Notes',  price: 3.49,  category: 'Stationery' },
];

let activeCategory = 'All';

function formatPrice(amount) {
  return '$' + amount.toFixed(2);
}

function getCategories() {
  const cats = products.map(p => p.category);
  return ['All', ...new Set(cats)];
}

function filterProducts(category) {
  if (category === 'All') return products;
  return products.filter(p => p.category === category);
}

function renderCard(product) {
  const article = document.createElement('article');
  const h2 = document.createElement('h2');
  h2.textContent = product.name;
  const price = document.createElement('p');
  price.textContent = formatPrice(product.price);
  const cat = document.createElement('p');
  cat.textContent = product.category;
  article.append(h2, price, cat);
  return article;
}

function renderAll() {
  const grid = document.getElementById('product-grid');
  grid.innerHTML = '';
  const filtered = filterProducts(activeCategory);
  filtered.forEach(p => grid.append(renderCard(p)));
}

function buildFilter() {
  const bar = document.getElementById('filter-bar');
  getCategories().forEach(cat => {
    const btn = document.createElement('button');
    btn.textContent = cat;
    btn.addEventListener('click', () => {
      activeCategory = cat;
      renderAll();
    });
    bar.append(btn);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  buildFilter();
  renderAll();
});
