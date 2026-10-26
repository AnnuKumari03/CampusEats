
const express = require('express');
const { ApolloServer } = require('@apollo/server');
const { expressMiddleware } = require('@as-integrations/express5');
const { readFileSync } = require('fs');
const path = require('path');
const cors = require('cors');
const pool = require('./db');

async function startServer() {
  const app = express();

  const typeDefs = readFileSync(
    path.join(__dirname, 'schema.graphql'),
    'utf8'
  );

  const resolvers = {
    Query: {
      menuItems: async () => {
        const [rows] = await pool.query(
          'SELECT id, name, category, price FROM menu_items'
        );
        return rows;
      },

      menuItem: async (_, { id }) => {
        const [rows] = await pool.execute(
          'SELECT id, name, category, price FROM menu_items WHERE id = ?',
          [id]
        );
        return rows[0] || null;
      }
    },

    Mutation: {
      addMenuItem: async (_, { name, category, price }) => {
        const [result] = await pool.execute(
          'INSERT INTO menu_items (name, category, price) VALUES (?, ?, ?)',
          [name, category, price]
        );

        const [rows] = await pool.execute(
          'SELECT id, name, category, price FROM menu_items WHERE id = ?',
          [result.insertId]
        );

        return rows[0];
      },

      updateMenuItem: async (_, { id, name, category, price }) => {
        const [result] = await pool.execute(
          'UPDATE menu_items SET name = ?, category = ?, price = ? WHERE id = ?',
          [name, category, price, id]
        );

        if (result.affectedRows === 0) {
          return null;
        }

        const [rows] = await pool.execute(
          'SELECT id, name, category, price FROM menu_items WHERE id = ?',
          [id]
        );

        return rows[0] || null;
      }
    }
  };

  const server = new ApolloServer({ typeDefs, resolvers });
  await server.start();

  app.use(cors());
  app.use(express.json());

  app.use('/graphql', expressMiddleware(server));

  app.use(express.static(path.join(__dirname, 'public')));

  app.listen(4000, () => {
    console.log('Server running at http://localhost:4000');
    console.log('GraphQL endpoint: http://localhost:4000/graphql');
  });
}

startServer().catch((error) => {
  console.error('Server failed to start:', error);
  process.exit(1);
});
