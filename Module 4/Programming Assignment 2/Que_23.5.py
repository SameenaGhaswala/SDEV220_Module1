import csv
import sqlite3

conn = sqlite3.connect("books.db")
curs = conn.cursor()

with open("books2.csv", "rt", newline="") as f:
    cin = csv.DictReader(f)

    for book in cin:
        curs.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (book["title"], book["author"], int(book["year"]))
        )

conn.commit()
conn.close()