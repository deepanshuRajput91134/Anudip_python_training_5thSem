#Library Book Search
''' _ _ _ _ _ _ _
• Display unavailable books.
• Find all books with more than 2 copies.
• Count available books.
• Stop searching once a requested book is found.
_ _ _ _ _ _ _ _ _ _'''
# Library Book Search

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Unavailable books
print("Unavailable Books:")

for book in books:
    if book[1] == 0:
        print(book[0])

# Books with more than 2 copies
print("\nBooks with more than 2 copies:")

for book in books:
    if book[1] > 2:
        print(book[0])

# Count available books
count = 0

for book in books:
    if book[1] > 0:
        count += 1

print("\nAvailable Books:", count)

# Search requested book
search = "Java Programming"

for book in books:
    if book[0] == search:
        print("\nBook Found:", book[0])
        break