# #Smart Electricity Billing System
# ''' __ _ _ _ _ _ __ _ _ _ __ _ _ _ _ _ __
# 1. Display houses consuming more than 400 units.
# 2. Find the highest-consuming house.
# 3. Find the lowest-consuming house.
# 4. Calculate the total units consumed.
# 5. Create separate lists for:
# o Low Consumption (< 200)
# o Medium Consumption (200–400)
# o High Consumption (> 400)
# 6. Count houses eligible for an energy-saving campaign (consumption > 300).
# _ _ _ _ __ _ _ _ _ __. _ _ _ _ _ __ _'''
# Smart Electricity Billing System

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

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# 2. Find the highest-consuming house
highest_house = max(units, key=units.get)
print("\nHighest Consumption:")
print(highest_house, "(", units[highest_house], "units )")

# 3. Find the lowest-consuming house
lowest_house = min(units, key=units.get)
print("\nLowest Consumption:")
print(lowest_house, "(", units[lowest_house], "units )")

# 4. Calculate the total units consumed
total_units = sum(units.values())
print("\nTotal Units Consumed:", total_units)

# 5. Create separate lists
low_consumption = []
medium_consumption = []
high_consumption = []

for house, unit in units.items():
    if unit < 200:
        low_consumption.append(house)
    elif 200 <= unit <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)

# 6. Count houses eligible for energy-saving campaign
count = 0
for unit in units.values():
    if unit > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)