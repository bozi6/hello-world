import sqlite3

conn = sqlite3.connect('ratings.db')
cur = conn.cursor()

cur.execute("""
SELECT * FROM ratings
    WHERE location=? AND rating = ?
""", (3,5))

print(cur.fetchall())
conn.close()
