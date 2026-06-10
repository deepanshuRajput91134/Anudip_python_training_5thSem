#Smart Library Management System
'''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
1. Add a book.
2. Remove a book.
3. Search a book by ID.
4. Search by title.
5. Update available copies.
6. Issue a book.
7. Return a book.
8. Display books with fewer than 3 copies.
9. Display books that are unavailable.
10. Find the most available book.
11. Generate a restocking report.
12. Create a separate dictionary of books requiring immediate purchase.
 _ _ _ _. __ _ _ _ _ _ _ __. __ '''
 # ==========================================
# Smart Library Management System
# ==========================================

library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Science", "author": "XYZ", "copies": 4},
    "B103": {"title": "Machine Learning", "author": "John", "copies": 6},
    "B104": {"title": "AI Fundamentals", "author": "David", "copies": 2},
    "B105": {"title": "Java Programming", "author": "Smith", "copies": 3},
    "B106": {"title": "C Programming", "author": "Alex", "copies": 7},
    "B107": {"title": "C++ Guide", "author": "Peter", "copies": 1},
    "B108": {"title": "Web Development", "author": "James", "copies": 5},
    "B109": {"title": "Database Systems", "author": "Kevin", "copies": 4},
    "B110": {"title": "Operating System", "author": "Robert", "copies": 3},
    "B111": {"title": "Networking", "author": "Tom", "copies": 2},
    "B112": {"title": "Cyber Security", "author": "Harry", "copies": 5},
    "B113": {"title": "Cloud Computing", "author": "Chris", "copies": 4},
    "B114": {"title": "Linux Essentials", "author": "Sam", "copies": 2},
    "B115": {"title": "Software Testing", "author": "Wilson", "copies": 6},
    "B116": {"title": "HTML & CSS", "author": "Martin", "copies": 7},
    "B117": {"title": "JavaScript", "author": "Clark", "copies": 3},
    "B118": {"title": "React JS", "author": "Daniel", "copies": 5},
    "B119": {"title": "Node JS", "author": "Joseph", "copies": 4},
    "B120": {"title": "Django", "author": "Anderson", "copies": 2},
    "B121": {"title": "Flask", "author": "Thomas", "copies": 1},
    "B122": {"title": "Data Structures", "author": "Jack", "copies": 6},
    "B123": {"title": "Algorithms", "author": "Ryan", "copies": 5},
    "B124": {"title": "Computer Graphics", "author": "Henry", "copies": 3},
    "B125": {"title": "Big Data", "author": "Scott", "copies": 4},
    "B126": {"title": "Blockchain", "author": "Victor", "copies": 2},
    "B127": {"title": "DevOps", "author": "George", "copies": 5},
    "B128": {"title": "AWS Guide", "author": "Steve", "copies": 4},
    "B129": {"title": "Azure Cloud", "author": "Mark", "copies": 2},
    "B130": {"title": "Google Cloud", "author": "Luke", "copies": 3}
}

# Display All Books
def display_books():
    print("\n===== Library Books =====")
    for bid, details in library.items():
        print(bid, details)

# Add Book
def add_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        print("Book ID Already Exists")
    else:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        copies = int(input("Enter Copies: "))

        library[bid] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book Added Successfully")

# Remove Book
def remove_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        del library[bid]
        print("Book Removed Successfully")
    else:
        print("Book Not Found")

# Search Book By ID
def search_by_id():
    bid = input("Enter Book ID: ")

    if bid in library:
        print(library[bid])
    else:
        print("Book Not Found")

# Search Book By Title
def search_by_title():
    title = input("Enter Book Title: ")

    found = False

    for bid, details in library.items():
        if details["title"].lower() == title.lower():
            print(bid, details)
            found = True

    if not found:
        print("Book Not Found")

# Update Copies
def update_copies():
    bid = input("Enter Book ID: ")

    if bid in library:
        copies = int(input("Enter New Copies: "))
        library[bid]["copies"] = copies
        print("Copies Updated Successfully")
    else:
        print("Book Not Found")

# Issue Book
def issue_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        if library[bid]["copies"] > 0:
            library[bid]["copies"] -= 1
            print("Book Issued Successfully")
        else:
            print("Book Not Available")
    else:
        print("Book Not Found")

# Return Book
def return_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        library[bid]["copies"] += 1
        print("Book Returned Successfully")
    else:
        print("Book Not Found")

# Books With Fewer Than 3 Copies
def fewer_than_3():
    print("\nBooks With Less Than 3 Copies")

    for bid, details in library.items():
        if details["copies"] < 3:
            print(bid, details)

# Unavailable Books
def unavailable_books():
    print("\nUnavailable Books")

    for bid, details in library.items():
        if details["copies"] == 0:
            print(bid, details)

# Most Available Book
def most_available():
    max_copies = -1
    book = ""

    for bid, details in library.items():
        if details["copies"] > max_copies:
            max_copies = details["copies"]
            book = bid

    print("Most Available Book:")
    print(book, library[book])

# Restocking Report
def restocking_report():
    print("\nRestocking Required")

    for bid, details in library.items():
        if details["copies"] < 3:
            print(bid, details)

# Immediate Purchase Dictionary
def immediate_purchase():
    purchase = {}

    for bid, details in library.items():
        if details["copies"] < 2:
            purchase[bid] = details

    print("\nBooks Requiring Immediate Purchase")
    print(purchase)

# Library Summary Report
def summary_report():
    print("\n===== Library Summary Report =====")
    most_available()
    restocking_report()
    immediate_purchase()

# Menu Driven Program
while True:

    print("\n===== Smart Library Management =====")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book By ID")
    print("5. Search Book By Title")
    print("6. Update Copies")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Books With Less Than 3 Copies")
    print("10. Unavailable Books")
    print("11. Most Available Book")
    print("12. Restocking Report")
    print("13. Immediate Purchase List")
    print("14. Library Summary Report")
    print("15. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books()
    elif choice == 2:
        add_book()
    elif choice == 3:
        remove_book()
    elif choice == 4:
        search_by_id()
    elif choice == 5:
        search_by_title()
    elif choice == 6:
        update_copies()
    elif choice == 7:
        issue_book()
    elif choice == 8:
        return_book()
    elif choice == 9:
        fewer_than_3()
    elif choice == 10:
        unavailable_books()
    elif choice == 11:
        most_available()
    elif choice == 12:
        restocking_report()
    elif choice == 13:
        immediate_purchase()
    elif choice == 14:
        summary_report()
    elif choice == 15:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")