#Mobile Contact Directory System
'''_ _ _ _ _ __ _ _ _ _ _ __ _ _ _ _ __
Create a menu-driven application to:
1. Display all contacts.
2. Search a contact by name.
3. Add a new contact.
4. Update an existing contact number.
5. Delete a contact.
6. Display contacts whose names start with a vowel.
7. Save all modifications back to the file.
 __ _ _ _ __ _. _ __ _ _ _ _ __ _ _ __ _ __ '''
import os

# File path
current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "contacts.txt")


# Read contacts from file
def read_contacts():

    contacts = []

    file = open(file_path, "r")

    for line in file:

        data = line.strip().split(",")

        contact = {
            "name": data[0],
            "number": data[1]
        }

        contacts.append(contact)

    file.close()

    return contacts


# Save contacts to file
def save_contacts(contacts):

    file = open(file_path, "w")

    for contact in contacts:

        file.write(
            f"{contact['name']},{contact['number']}\n"
        )

    file.close()


# Display all contacts
def display_contacts():

    contacts = read_contacts()

    print("\nContact List")
    print("-" * 40)

    for contact in contacts:

        print(
            contact["name"],
            contact["number"]
        )


# Search contact
def search_contact():

    contacts = read_contacts()

    name = input("Enter Contact Name: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("\nContact Found")
            print("Name :", contact["name"])
            print("Number :", contact["number"])

            found = True
            break

    if not found:
        print("Contact Not Found")


# Add contact
def add_contact():

    contacts = read_contacts()

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    contacts.append({
        "name": name,
        "number": number
    })

    save_contacts(contacts)

    print("Contact Added Successfully")


# Update contact
def update_contact():

    contacts = read_contacts()

    name = input("Enter Contact Name: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            new_number = input(
                "Enter New Mobile Number: "
            )

            contact["number"] = new_number

            found = True

            break

    if found:

        save_contacts(contacts)

        print("Contact Updated Successfully")

    else:

        print("Contact Not Found")


# Delete contact
def delete_contact():

    contacts = read_contacts()

    name = input("Enter Contact Name: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            found = True

            break

    if found:

        save_contacts(contacts)

        print("Contact Deleted Successfully")

    else:

        print("Contact Not Found")


# Display names starting with vowels
def contacts_starting_with_vowel():

    contacts = read_contacts()

    print("\nContacts Starting With Vowel")
    print("-" * 40)

    vowels = "AEIOU"

    for contact in contacts:

        if contact["name"][0].upper() in vowels:

            print(
                contact["name"],
                contact["number"]
            )


# Main Menu
while True:

    print("\n===== Mobile Contact Directory =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        contacts_starting_with_vowel()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")