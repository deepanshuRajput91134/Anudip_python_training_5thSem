#Library Book Availability
'''_ _ _ _ __ _ _ _ __ _ _ __ _
• Display books that are currently unavailable.
• Count the number of available books.
• Find the book with the maximum copies.
• Create a list of books having less than 3 copies.
• Calculate the total number of books available.
_ _ _ _ _ _ _ _ __. _ __ _. _ _'''
# Dictionary storing books and copies
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display unavailable books
print("Unavailable books:")

for book, copies in books.items():
    if copies == 0:
        print(book)

# Count available books
count = 0

for copies in books.values():
    if copies > 0:
        count += 1

print("\nAvailable books count:", count)

# Find book with maximum copies
maximum = max(books, key=books.get)

print("\nBook with maximum copies:")
print(maximum, ":", books[maximum])

# Create list of books having less than 3 copies
less_books = []

for book, copies in books.items():
    if copies < 3:
        less_books.append(book)

print("\nBooks having less than 3 copies:")
print(less_books)

# Calculate total books available
total = sum(books.values())

print("\nTotal books available:", total)