#Electricity Consumption Report
'''_. _ __ _ _ _ __ _ _ __. __ _ __
• Display houses consuming more than 300 units.
• Count houses consuming less than 200 units.
• Find the house with the highest consumption.
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).
• Categorize houses as:
o Low: < 200 units
o Medium: 200–350 units
o High: > 350 units
_ _. _ _ _ __ _ __ _ _ _ __ _ __ __ '''
# Dictionary storing electricity units
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Display houses consuming more than 300 units
print("Houses consuming more than 300 units:")

for house, unit in units.items():
    if unit > 300:
        print(house, ":", unit)

# Count houses consuming less than 200 units
count = 0

for unit in units.values():
    if unit < 200:
        count += 1

print("\nHouses consuming less than 200 units:", count)

# Find house with highest consumption
highest = max(units, key=units.get)

print("\nHouse with highest consumption:")
print(highest, ":", units[highest])

# Create list for awareness campaign
campaign = []

for house, unit in units.items():
    if unit > 400:
        campaign.append(house)

print("\nHouses eligible for awareness campaign:")
print(campaign)

# Categorize houses
print("\nHouse Categories:")

for house, unit in units.items():

    # Low consumption
    if unit < 200:
        category = "Low"

    # Medium consumption
    elif 200 <= unit <= 350:
        category = "Medium"

    # High consumption
    else:
        category = "High"

    print(house, ":", category)