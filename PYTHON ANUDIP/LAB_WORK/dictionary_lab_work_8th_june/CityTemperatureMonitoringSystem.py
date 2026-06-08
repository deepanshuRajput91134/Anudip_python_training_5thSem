#City Temperature Monitoring System
'''_. _ _ ___ _ __ _ _ _ __ _ __
1. Display cities having temperature above 40°C.
2. Find the hottest city.
3. Find the coolest city.
4. Calculate average temperature.
5. Create a list of pleasant cities (temperature < 35°C).
6. Count cities with temperature between 35°C and 40°C.
_ __ _ _ __ _ _ __ _ _ __ __ _ __ _ _ __ _ __'''
# Dictionary storing city temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Display cities above 40 degree Celsius
print("Cities Above 40°C:")

for city, temp in temperature.items():
    if temp > 40:
        print(city)

# Find hottest city
hot = max(temperature, key=temperature.get)

print("\nHottest City:")
print(hot, "(", temperature[hot], "°C )")

# Find coolest city
cool = min(temperature, key=temperature.get)

print("\nCoolest City:")
print(cool, "(", temperature[cool], "°C )")

# Calculate average temperature
average = sum(temperature.values()) / len(temperature)

print("\nAverage Temperature:", average)

# Create list of pleasant cities
pleasant = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)

print("\nPleasant Cities:")
print(pleasant)

# Count cities between 35 and 40
count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)