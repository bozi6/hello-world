import sqlite3

conn = sqlite3.connect('ratings.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

