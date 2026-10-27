import csv

with open("books.csv", "rt") as f:
    cin = csv.DictReader(f)
    books = [book for book in cin]

print(books)


