# Read SQL files from Python.

import sqlite3

conn = sqlite3.connect('album2.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM artist')
artists = cursor.fetchall()
print(artists)

cursor.execute('SELECT name FROM artist')
name_artists = cursor.fetchall()
print(name_artists)

albums_CD = cursor.execute('SELECT title FROM album a JOIN artist ar ON a.artist_id = ar.artist_id AND ar.name = "Celine Dion"').fetchall()
print(albums_CD)

conn.close()