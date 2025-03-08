import sqlite3

conn = sqlite3.connect('movies.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        overview TEXT,
        img_url TEXT,
        href TEXT
    )
''')


conn.commit()
conn.close()


