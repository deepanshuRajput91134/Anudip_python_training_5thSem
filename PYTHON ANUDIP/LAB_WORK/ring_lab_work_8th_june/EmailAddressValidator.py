#Email Address Validator
# ''' __ ___ __ _ _ __ _ _ _ ___ ___ _ _ __ _ __ _ _ __ _ _
# 1. Extract username.
# 2. Extract domain name.
# 3. Extract extension.
# 4. Count digits present in username.
# 5. Count special characters.
# 6. Check whether:
# o Exactly one '@' exists.
# o At least one '.' exists after '@'.
# 7. Display Valid Email or Invalid Email.
#  __ _ _ _ __ _ _ _ _ _ _ __. __ _ __ _ _ _ _'''
email = "rahul.sharma2026@gmail.com"

print("Email:", email)

# Extract username
username = email.split("@")[0]

print("Username:", username)

# Extract domain and extension
domain_part = email.split("@")[1]

domain = domain_part.split(".")[0]
extension = domain_part.split(".")[1]

print("Domain:", domain)
print("Extension:", extension)

# Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

print("Digits Found:", digit_count)

# Count special characters
special = 0

for ch in email:
    if not ch.isalnum():
        special += 1

print("Special Characters Found:", special)

# Validate email
if email.count("@") == 1 and "." in domain_part:
    print("Email Status: Valid")

else:
    print("Email Status: Invalid")