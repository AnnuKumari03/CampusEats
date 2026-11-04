// server.js -- CampusEats Catalogue REST API (Node + Express)
const express = require('express');
const app = express();

app.use(express.json());
app.use(express.static('public'));

// In-memory catalogue data used as the source of truth for this assignment.
let items = [
  { id: 1, name: 'Veg Thali', price: 90, available: true },
  { id: 2, name: 'Paneer Roll', price: 70, available: true },
  { id: 3, name: 'Masala Dosa', price: 60, available: false },
  { id: 4, name: 'Cold Coffee', price: 80, available: true }
];
let nextId = 5;

// GET /items
app.get('/items', (req, res) => {
  res.status(200).json(items);
});

// GET /items/:id
app.get('/items/:id', (req, res) => {
  const item = items.find(i => i.id === Number(req.params.id));
  if (!item) return res.status(404).json({ error: 'not found' });
  res.status(200).json(item);
});

// DELETE /items/:id
app.delete('/items/:id', (req, res) => {
  const itemIndex = items.findIndex(i => i.id === Number(req.params.id));
  if (itemIndex === -1) return res.status(404).json({ error: 'not found' });

  items.splice(itemIndex, 1);
  res.status(204).end();
});

// POST /items
app.post('/items', (req, res) => {
  const { name, price, available } = req.body;

  if (!name || String(name).trim() === '') {
    return res.status(422).json({ error: 'name required' });
  }

  const parsedPrice = Number(price);
  const item = {
    id: nextId++,
    name: String(name).trim(),
    price: Number.isFinite(parsedPrice) ? parsedPrice : 0,
    available: Boolean(available)
  };

  items.push(item);
  res.status(201).json(item);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Catalogue on http://localhost:${port}`));
