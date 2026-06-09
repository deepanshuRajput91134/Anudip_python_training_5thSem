# Username Generator System
'''_ _ _ _ _ _ __ __ ___ _ __ 
Generate a username using the rules:
1. Remove spaces.
2. Convert to lowercase.
3. Append current year (2026).
4. If username length exceeds 12, keep only first 12 characters.
5. Count vowels in the generated username.
6. Count consonants.
7. Display username statistics.
_ _ _ _ __ _ _ _ _ _ __ _ _ _ _'''
# Student name
name = "Rahul Sharma"

print("Original Name:", name)

# Remove spaces
username = name.replace(" ", "")

# Convert to lowercase
username = username.lower()

# Append current year
username = username + "2026"

print("Generated Username:")
print(username)

# Username length
length = len(username)

print("Username Length:", length)

# Keep only first 12 characters if length exceeds 12
if len(username) > 12:
    short_username = username[:12]

    print("Short Username:")
    print(short_username)

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

print("Status: Username Generated Successfully")