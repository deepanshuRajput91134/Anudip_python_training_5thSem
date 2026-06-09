#Employee ID Validation and Analysis System
'''_ _ _ _ _ __ _ __ _ _ __ _ _ _ __ __
1. Count the number of uppercase letters.
2. Count the number of digits.
3. Extract the joining year.
4. Extract the employee name.
5. Check whether the ID follows these rules:
o Starts with "EMP"
o Contains exactly 4 digits for the year
o Ends with exactly 3 digits
6. Create a list containing all digits present in the ID.
7. Find the sum of all digits present in the ID.
8. Display whether the ID is valid or invalid.
_. __ _ _ _ __ _ _ _ __ _ _ __ _ '''
# Employee ID
emp_id = "EMP2026ANUJ458"

print("Employee ID:", emp_id)

# Count uppercase letters
upper = 0

for ch in emp_id:
    if ch.isupper():
        upper += 1

print("Uppercase Letters:", upper)

# Count digits
digits = 0

for ch in emp_id:
    if ch.isdigit():
        digits += 1

print("Digits:", digits)

# Extract joining year
year = emp_id[3:7]

print("Joining Year:", year)

# Extract employee name
name = emp_id[7:-3]

print("Employee Name:", name)

# Create list of digits
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

print("Digit List:", digit_list)

# Find sum of digits
total = sum(digit_list)

print("Sum of Digits:", total)

# Validate employee ID
if emp_id.startswith("EMP") and year.isdigit() and emp_id[-3:].isdigit():
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")