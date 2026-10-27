// server.js -- the GraphQL API for CS543 Campus Library
// Architecture: Browser (fetch) -> GraphQL API (Apollo) -> Resolvers -> MySQL (mysql2)

require('dotenv').config();
const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const pool = require('./db');

// 1. The Schema: Defines types, queries, and mutations offered by the API
const typeDefs = `#graphql
  type Author {
    id: ID!
    name: String!
    country: String
    books: [Book!]!
  }

  type Book {
    id: ID!
    title: String!
    year: Int
    author: Author!
  }

  type Query {
    authors: [Author!]!
    author(id: ID!): Author
    books: [Book!]!
  }

  type Mutation {
    addBook(title: String!, year: Int, authorId: ID!): Book!
  }
`;

// 2. The Resolvers: How each field gets its data from MySQL
const resolvers = {
  Query: {
    // Fetch all authors from MySQL
    authors: async () => {
      try {
        const [rows] = await pool.query('SELECT * FROM authors');
        return rows;
      } catch (err) {
        console.error('Error in Query.authors resolver:', err.message);
        throw new Error(`Database error fetching authors: ${err.message}`);
      }
    },

    // Fetch a single author by ID using parameterized query
    author: async (_parent, { id }) => {
      try {
        const [rows] = await pool.query('SELECT * FROM authors WHERE id = ?', [id]);
        return rows[0] || null;
      } catch (err) {
        console.error(`Error in Query.author resolver for id ${id}:`, err.message);
        throw new Error(`Database error fetching author: ${err.message}`);
      }
    },

    // Fetch all books from MySQL
    books: async () => {
      try {
        const [rows] = await pool.query('SELECT * FROM books');
        return rows;
      } catch (err) {
        console.error('Error in Query.books resolver:', err.message);
        throw new Error(`Database error fetching books: ${err.message}`);
      }
    },
  },

  // Relationship resolvers: Nested Author -> Books
  Author: {
    books: async (author) => {
      try {
        const [rows] = await pool.query('SELECT * FROM books WHERE author_id = ?', [author.id]);
        return rows;
      } catch (err) {
        console.error(`Error in Author.books resolver for author ${author.id}:`, err.message);
        throw new Error(`Database error resolving books for author: ${err.message}`);
      }
    },
  },

  // Relationship resolvers: Nested Book -> Author
  Book: {
    author: async (book) => {
      try {
        const [rows] = await pool.query('SELECT * FROM authors WHERE id = ?', [book.author_id]);
        return rows[0];
      } catch (err) {
        console.error(`Error in Book.author resolver for book ${book.id}:`, err.message);
        throw new Error(`Database error resolving author for book: ${err.message}`);
      }
    },
  },

  // Mutation: Inserts a new book and returns the newly created record
  Mutation: {
    addBook: async (_parent, { title, year, authorId }) => {
      try {
        // Parameterized INSERT query to avoid SQL injection
        const [result] = await pool.query(
          'INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)',
          [title.trim(), year || null, authorId]
        );

        // Fetch and return the newly inserted book
        const [rows] = await pool.query('SELECT * FROM books WHERE id = ?', [result.insertId]);
        return rows[0];
      } catch (err) {
        console.error('Error in Mutation.addBook resolver:', err.message);
        throw new Error(`Database error adding book: ${err.message}`);
      }
    },
  },
};

// 3. Start the Apollo Standalone Server
async function start() {
  const server = new ApolloServer({
    typeDefs,
    resolvers,
  });

  const port = Number(process.env.PORT) || 4000;
  const { url } = await startStandaloneServer(server, {
    listen: { port },
  });

  console.log(`\n======================================================`);
  console.log(`🚀 CS543 Campus Library GraphQL API Ready!`);
  console.log(`📡 GraphQL API & Apollo Sandbox: ${url}`);
  console.log(`🗄️ Connected to MySQL database: ${process.env.DB_NAME || 'gqldemo'}`);
  console.log(`======================================================\n`);
}

start().catch((err) => {
  console.error('Failed to start Apollo Server:', err);
});
