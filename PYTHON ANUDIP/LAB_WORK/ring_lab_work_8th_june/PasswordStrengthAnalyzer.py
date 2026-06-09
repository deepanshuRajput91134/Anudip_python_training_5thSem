#Password Strength Analyzer
'''  _ __ _ _ _ _ _ _ __ _ _. __ _ _ _ _ __ __ _ _ _
Write a program to determine whether the password is Strong, Medium, or Weak.
Rules:
• Minimum length 8
• Contains at least:
o 1 uppercase letter
o 1 lowercase letter
o 1 digit
o 1 special character
Additionally:
1. Count uppercase letters.
2. Count lowercase letters.
3. Count digits.
4. Count special characters.
5. Display all digits separately.
6. Display all special characters separately.
_ _ _ __ _ __ _ _ _ _ __ _ _ _ _ _ _'''
# Password input
password = "Python@2026!"

print("Password:", password)

# Variables
upper = 0
lower = 0
digits = 0
special = 0

digit_list = []
special_list = []

# Analyze password
for ch in password:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)

    else:
        special += 1
        special_list.append(ch)

# Display counts
print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Special Characters:", special)

# Display digits and special characters
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)

# Check password strength
if len(password) >= 8 and upper >= 1 and lower >= 1 and digits >= 1 and special >= 1:
    print("Password Strength: Strong")

elif len(password) >= 6:
    print("Password Strength: Medium")

else:
    print("Password Strength: Weak")