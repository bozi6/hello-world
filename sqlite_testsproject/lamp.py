import sqlite3

conn = sqlite3.connect('ratings.db')
cur = conn.cursor()


def multilpesearch(location, rating):
    cur.execute("""
    SELECT * FROM ratings
        WHERE location=? AND rating = ?
    """, (location, rating))
    return cur.fetchall()

def likesearch(location):
    cur.execute("""
    SELECT * FROM ratings
        WHERE location = ?
    """, (location,))
    return cur.fetchall()

def deleteonerecord(id):
    cur.execute("""
    DELETE FROM ratings
        WHERE id = ?
    """, (id,))
    conn.commit()

def deleteallrecord():
    cur.execute("""
    DELETE FROM ratings
    """)
    conn.commit()

def droptable():
    cur.execute("""
    DROP TABLE ratings
    """)
    conn.commit()

def modifyrecord(id, location, rating):
    cur.execute("""
    UPDATE ratings
        SET location = ?, rating = ?
        WHERE id = ?
    """, (location, rating, id))
    conn.commit()

def readid(id):
    cur.execute("""
    SELECT * FROM ratings
        WHERE id = ?
    """, (id,))
    return cur.fetchall()

def orderrecords():
    cur.execute("""
    SELECT * FROM ratings
        ORDER BY created DESC
    """)
    return cur.fetchall()

def recordnumbers():
    cur.execute("""
    SELECT COUNT(*) FROM ratings
    """)
    return cur.fetchone()[0]

def avreagerecords():
    cur.execute("""
    SELECT AVG(rating) FROM ratings
    """)
    return cur.fetchone()[0]

def grouprecords():
    cur.execute("""
    SELECT location, 
           COUNT(*),
           AVG(rating) 
    FROM ratings
    GROUP BY location
    """)
    return cur.fetchall()

ga = grouprecords()
for row in ga:
    print(row)
