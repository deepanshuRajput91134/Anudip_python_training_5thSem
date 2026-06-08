#Smart Electricity Billing System
'''_ _ _ __ _ _ _ _ _ _ _ __ 
1. Display houses consuming more than 400 units.
2. Find the highest-consuming house.
3. Find the lowest-consuming house.
4. Calculate total units consumed.
5. Create lists:
o Low Consumption (< 200)
o Medium Consumption (200–400)
o High Consumption (> 400)
6. Count houses eligible for an energy-saving campaign (consumption > 300).
_ _ _ _ _ _ _ _ _. __ _ _ _. __ _ _ _ __ _ _ _'''
# Dictionary storing electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house, unit in units.items():
    if unit > 400:
        print(house)

# Find highest-consuming house
highest = max(units, key=units.get)

print("\nHighest Consumption:")
print(highest, "(", units[highest], "units )")

# Find lowest-consuming house
lowest = min(units, key=units.get)

print("\nLowest Consumption:")
print(lowest, "(", units[lowest], "units )")

# Calculate total units consumed
total = sum(units.values())

print("\nTotal Units Consumed:", total)

# Create consumption category lists
low = []
medium = []
high = []

for house, unit in units.items():

    # Low consumption
    if unit < 200:
        low.append(house)

    # Medium consumption
    elif 200 <= unit <= 400:
        medium.append(house)

    # High consumption
    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# Count houses eligible for campaign
count = 0

for unit in units.values():
    if unit > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)