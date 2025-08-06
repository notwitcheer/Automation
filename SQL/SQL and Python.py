# SQL and Python.

import sqlite3

conn = sqlite3.connect('album2.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE artist (
    artist_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR
)
''')

cursor.execute('''
CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    title VARCHAR,
    release_date INTEGER
)
''')

cursor.execute('''
INSERT INTO artist (name) VALUES ('Michael Jackson')
''')
mj_id = cursor.lastrowid

cursor.execute('INSERT INTO album (artist_id, title, release_date) VALUES (' + str(mj_id) + ', "Thriller", 1982)')

cursor.execute('''
INSERT INTO artist (name) VALUES ('Celine Dion')
''')
cd_id = cursor.lastrowid

cursor.execute('INSERT INTO album (artist_id, title, release_date) VALUES (' + str(cd_id) + ', "Falling Into You", 1996)')

cursor.execute('INSERT INTO album (artist_id, title, release_date) VALUES (' + str(cd_id) + ',"Lets Talk About Love", 1997)')

conn.commit()
conn.close()