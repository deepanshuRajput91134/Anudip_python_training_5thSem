#Mobile Contact Directory
''' _ __ _ _ _ __ _. __ _ _ __ 
• Display all contact names in alphabetical order.
• Count the total number of contacts.
• Search for a given contact name.
• Create a list of contacts whose names start with a vowel.
• Stop the search using break once the required contact is found.
_. __ _ _ __ _ _ __ _ __ _ _ __ _ _'''
# Dictionary storing contact details
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display contact names in alphabetical order
print("Contact names in alphabetical order:")

for name in sorted(contacts):
    print(name)

# Count total contacts
total = len(contacts)

print("\nTotal number of contacts:", total)

# Search for a contact
search = input("\nEnter contact name to search: ")

found = False

for name, number in contacts.items():

    # Stop search when contact is found
    if name == search:
        print("Contact Found")
        print(name, ":", number)
        found = True
        break

# If contact not found
if found == False:
    print("Contact not found")

# Create list of contacts starting with vowels
vowels = []

for name in contacts:

    if name[0].lower() in "aeiou":
        vowels.append(name)

print("\nContacts starting with vowels:")
print(vowels)