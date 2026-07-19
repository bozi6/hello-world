import sqlite3

adatok = [
    (1, 5),
    (2, 4),
    (5, 2),
    (6, 1),
]

conn = sqlite3.connect('ratings.db')
cur = conn.cursor()

cur.executemany("""
INSERT INTO ratings (location, rating) VALUES (?, ?)
""", adatok)

conn.commit()
conn.close()
