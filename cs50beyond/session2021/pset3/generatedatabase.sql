-- Open a PostgreSQL terminal using the URI from Heroku's database credentials:
-- psql postgres://tdpmrxyzqtyhfx:6d929e192d129a30f2fe22aec6afcf7ee2846995a004b6b5d497ffd863b31065@ec2-52-7-115-250.compute-1.amazonaws.com:5432/d79r0a8uiur6km
-- Create the database tables and populate them with data by running the following sql script:
-- psql> \i generatedatabase.sql
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    isbn VARCHAR NOT NULL,
    author_id INTEGER REFERENCES authors(id)
);

