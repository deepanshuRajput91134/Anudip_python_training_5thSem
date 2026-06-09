# #License Key Verification System
# '''_ _ _ _ _ _ _ _ __ ___ __ _ __ _ _ 
# 1. Verify there are exactly 4 groups.
# 2. Verify each group contains exactly 4 characters.
# 3. Count total letters.
# 4. Count vowels.
# 5. Remove hyphens and display the merged key.
# 6. Create a list containing all groups.
# 7. Display whether the key format is valid.
# _ _ __ _ _ _ __. __ _ _ _ __ _ _ ___ '''
# License key
license_key = "ABCD-EFGH-IJKL-MNOP"

print("License Key:")
print(license_key)

# Create list of groups
groups = license_key.split("-")

print("Groups:")
print(groups)

# Count groups
print("Number of Groups:", len(groups))

# Count total letters
letters = 0

for ch in license_key:

    if ch.isalpha():
        letters += 1

print("Total Letters:", letters)

# Count vowels
vowels = 0

for ch in license_key:

    if ch.lower() in "aeiou":
        vowels += 1

print("Total Vowels:", vowels)

# Remove hyphens
merged = license_key.replace("-", "")

print("Merged Key:")
print(merged)

# Validate license key
valid = True

if len(groups) != 4:
    valid = False

for group in groups:

    if len(group) != 4:
        valid = False

# Display result
if valid:
    print("License Key Status: Valid")

else:
    print("License Key Status: Invalid")