#Library Book Issue System
'''_ _ _. _ _ _ __ _ _. _ __ _ _ 
Develop a program to:
1. Display all books.
2. Search a book using Book ID.
3. Issue a book (decrease quantity by 1).
4. Return a book (increase quantity by 1).
5. Display unavailable books.
6. Display books requiring restocking (copies < 2).
7. Update the file after every issue/return operation.
 __ _ _ _ _ _ __ _ _ __ _ __ _ _ __ '''
import os

# File path
current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "books.txt")


# Read books from file
def read_books():
    books = []

    file = open(file_path, "r")

    for line in file:
        data = line.strip().split(",")

        book = {
            "id": data[0],
            "title": data[1],
            "quantity": int(data[2])
        }

        books.append(book)

    file.close()

    return books


# Update file
def update_file(books):
    file = open(file_path, "w")

    for book in books:
        file.write(
            f"{book['id']},{book['title']},{book['quantity']}\n"
        )

    file.close()


# Display all books
def display_books():
    books = read_books()

    print("\nBook Records")
    print("-" * 50)

    for book in books:
        print(book["id"], book["title"], book["quantity"])


# Search book
def search_book():
    books = read_books()

    book_id = input("Enter Book ID: ")

    found = False

    for book in books:
        if book["id"] == book_id:

            print("\nBook Found")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Quantity:", book["quantity"])

            found = True
            break

    if not found:
        print("Book Not Found")


# Issue book
def issue_book():
    books = read_books()

    book_id = input("Enter Book ID to Issue: ")

    for book in books:

        if book["id"] == book_id:

            if book["quantity"] > 0:

                book["quantity"] -= 1

                update_file(books)

                print("Book Issued Successfully")

            else:
                print("Book Not Available")

            return

    print("Book Not Found")


# Return book
def return_book():
    books = read_books()

    book_id = input("Enter Book ID to Return: ")

    for book in books:

        if book["id"] == book_id:

            book["quantity"] += 1

            update_file(books)

            print("Book Returned Successfully")

            return

    print("Book Not Found")


# Unavailable books
def unavailable_books():
    books = read_books()

    print("\nUnavailable Books")
    print("-" * 50)

    for book in books:

        if book["quantity"] == 0:
            print(book["id"], book["title"])


# Restocking required
def restock_books():
    books = read_books()

    print("\nBooks Requiring Restocking")
    print("-" * 50)

    for book in books:

        if book["quantity"] < 2:
            print(
                book["id"],
                book["title"],
                "Copies:",
                book["quantity"]
            )


# Main Menu
while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restock_books()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")