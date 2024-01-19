brew services start postgresql

initdb ./data
createdb movie_db
createuser -s vyl

psql -U vyl -d movie_db

\i schema/movie.sql

brew services stop postgresql
