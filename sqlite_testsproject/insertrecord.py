import sqlite3

conn = sqlite3.connect('ratings.db')
cur = conn.cursor()

cur.execute("""
INSERT INTO ratings (location, rating) VALUES (?, ?)
""", (1, 2))

conn.commit()
conn.close()
