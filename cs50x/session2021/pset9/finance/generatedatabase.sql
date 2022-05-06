CREATE TABLE users (id INTEGER, username TEXT NOT NULL, hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00, PRIMARY KEY(id));
CREATE UNIQUE INDEX username ON users (username);
CREATE TABLE portfolio (id INTEGER, user_id INTEGER, symbol TEXT NOT NULL, quantity INTEGER NOT NULL, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id));
CREATE TABLE transactions (id INTEGER, user_id INTEGER, symbol TEXT NOT NULL, quantity INTEGER NOT NULL, price REAL NOT NULL, occurrence TEXT NOT NULL, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id));
