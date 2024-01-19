CREATE TABLE movie (
 movie_id SERIAL PRIMARY KEY,
 movie_name VARCHAR(50) NOT NULL
);

-- Affects inserts, updated, deletes, but improves look-up
-- e.g. WHERE, JOIN, ORDER BY which used to require sequential
-- scan.
--
-- We're essentially using a b-tree here using varchar order,
-- whose value points at the data page with the row.
CREATE INDEX movie_name_index ON movie(movie_name);
