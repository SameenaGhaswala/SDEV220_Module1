import sqlite3

conn = sqlite3.connect("books.db")
curs = conn.cursor()

curs.execute("SELECT title FROM books ORDER BY title")

for row in curs.fetchall():
    print(row)

conn.close()