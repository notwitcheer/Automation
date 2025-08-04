# SQL.

# INTEGER : int
# VARCHAR : str


artist
- artist_id
- name 

album
- album_id
- artist_id
- title
- release date

CREATE TABLE artist(artist_id INTEGER NOT NULL PRIMARY KEY, name VARCHAR);

CREATE TABLE album(album_id INTEGER NOT NULL PRIMARY KEY, artist_id INTEGER NOT NULL, title VARCHAR, release_date INTEGER);

INSERT INTO artist (name) VALUES ('Michael Jackson');
INSERT INTO album (artist_id, title, release_date) VALUES (1, 'Thriller', 1983);

UPDATE album SET release_date = 1982 WHERE title = 'Thriller';

SELECT * FROM artist
SELECT name FROM artist
SELECT * FROM album WHERE release_date > 1990;

SELECT name, title FROM album a JOIN artist ar ON a.artist_id = ar.artist_id
SELECT title FROM album a JOIN artist ar ON a.artist_id = ar.artist_id AND ar.name = 'Celine Dion'