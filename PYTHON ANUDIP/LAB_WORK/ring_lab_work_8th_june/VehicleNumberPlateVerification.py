# Vehicle Number Plate Verification
'''_ _ _ _. __ _ _ _ __ _. __ 
1. Extract state code.
2. Extract district code.
3. Extract vehicle series.
4. Extract vehicle number.
5. Count letters and digits separately.
6. Verify:
o First 2 characters must be alphabets.
o Next 2 must be digits.
o Next 2 must be alphabets.
o Last 4 must be digits.
7. Display whether the number plate is valid.
 __ _ __ _ _ ___ __ _ _ _ __ _ __ _ _'''
# Vehicle number plate
vehicle = "MH12AB4589"

print("Vehicle Number:", vehicle)

# Extract details
state = vehicle[:2]
district = vehicle[2:4]
series = vehicle[4:6]
number = vehicle[6:]

# Display extracted values
print("State Code:", state)
print("District Code:", district)
print("Series:", series)
print("Vehicle Number:", number)

# Count letters and digits
letters = 0
digits = 0

for ch in vehicle:

    if ch.isalpha():
        letters += 1

    elif ch.isdigit():
        digits += 1

print("Total Letters:", letters)
print("Total Digits:", digits)

# Validate vehicle number
if (vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:6].isalpha() and
    vehicle[6:].isdigit()):

    print("Vehicle Number Status: Valid")

else:
    print("Vehicle Number Status: Invalid")