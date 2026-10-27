import sqlite3

conn = sqlite3.connect("books.db")
curs = conn.cursor()

curs.execute("SELECT * FROM books ORDER BY year")

for row in curs.fetchall():
    print(row)

conn.close()