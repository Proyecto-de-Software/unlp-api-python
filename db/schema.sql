DROP TABLE IF EXISTS issues;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS statuses;
DROP TABLE IF EXISTS users;

CREATE TABLE issues (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  category_id INTEGER NOT NULL,
  status_id INTEGER NOT NULL,
  FOREIGN KEY (category_id) REFERENCES categories (id),
  FOREIGN KEY (status_id) REFERENCES statuses (id)
);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE statuses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password TEXT UNIQUE NOT NULL,
  first_name TEXT UNIQUE NOT NULL,
  last_name TEXT UNIQUE NOT NULL
);
