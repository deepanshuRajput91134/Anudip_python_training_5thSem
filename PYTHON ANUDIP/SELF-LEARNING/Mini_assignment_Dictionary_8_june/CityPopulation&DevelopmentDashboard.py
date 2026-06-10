#City Population & Development Dashboard
'''___. _ __ _ _. _ _ _ _ _ _ _ _ _ 
1. Display all city details.
2. Find the most populated city.
3. Find the least populated city.
4. Calculate average population.
5. Display cities with literacy rate above 90%.
6. Display cities with literacy below average.
7. Calculate population density.
8. Find city with highest density.
9. Categorize cities:
o Small
o Medium
o Large
10. Create a development-priority list.
11. Generate separate dictionaries for:
o High Literacy Cities
o Low Literacy Cities
12. Generate a national summary report.
__ _ _ _ _ _ _ _ _ _ _ __ _ _ _ '''
# ==========================================
# City Population & Development Dashboard
# ==========================================

cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 92},
    "Bangalore": {"population": 13000000, "area": 709, "literacy": 90},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 89},
    "Pune": {"population": 7000000, "area": 516, "literacy": 91},
    "Jaipur": {"population": 4100000, "area": 467, "literacy": 84},
    "Lucknow": {"population": 3800000, "area": 631, "literacy": 82},
    "Kanpur": {"population": 3200000, "area": 403, "literacy": 81},
    "Nagpur": {"population": 2900000, "area": 218, "literacy": 89},
    "Indore": {"population": 3400000, "area": 530, "literacy": 87},
    "Bhopal": {"population": 2500000, "area": 285, "literacy": 85},
    "Patna": {"population": 2600000, "area": 250, "literacy": 83},
    "Surat": {"population": 7000000, "area": 461, "literacy": 89},
    "Agra": {"population": 1900000, "area": 188, "literacy": 80},
    "Varanasi": {"population": 1700000, "area": 112, "literacy": 81},
    "Meerut": {"population": 1600000, "area": 141, "literacy": 79},
    "Amritsar": {"population": 1200000, "area": 139, "literacy": 86},
    "Ludhiana": {"population": 1800000, "area": 159, "literacy": 85},
    "Ranchi": {"population": 1500000, "area": 175, "literacy": 84},
    "Raipur": {"population": 1400000, "area": 226, "literacy": 86},
    "Guwahati": {"population": 1200000, "area": 216, "literacy": 88},
    "Dehradun": {"population": 1100000, "area": 308, "literacy": 90},
    "Shimla": {"population": 200000, "area": 35, "literacy": 94},
    "Panaji": {"population": 150000, "area": 36, "literacy": 95},
    "Jodhpur": {"population": 1200000, "area": 233, "literacy": 82},
    "Udaipur": {"population": 500000, "area": 64, "literacy": 89},
    "Mysore": {"population": 1000000, "area": 128, "literacy": 91},
    "Coimbatore": {"population": 1800000, "area": 246, "literacy": 92}
}

# Display All Cities
def display_cities():
    for city, details in cities.items():
        print(city, details)

# Most Populated City
def most_populated():
    max_pop = -1
    city_name = ""

    for city, details in cities.items():
        if details["population"] > max_pop:
            max_pop = details["population"]
            city_name = city

    print("Most Populated City:", city_name, "-", max_pop)

# Least Populated City
def least_populated():
    min_pop = 999999999
    city_name = ""

    for city, details in cities.items():
        if details["population"] < min_pop:
            min_pop = details["population"]
            city_name = city

    print("Least Populated City:", city_name, "-", min_pop)

# Average Population
def average_population():
    total = 0

    for details in cities.values():
        total += details["population"]

    avg = total / len(cities)

    print("Average Population =", avg)

# Literacy Above 90%
def high_literacy():
    print("\nCities With Literacy Above 90%")

    for city, details in cities.items():
        if details["literacy"] > 90:
            print(city, details["literacy"])

# Literacy Below Average
def literacy_below_average():
    total = 0

    for details in cities.values():
        total += details["literacy"]

    avg = total / len(cities)

    print("\nCities With Literacy Below Average")

    for city, details in cities.items():
        if details["literacy"] < avg:
            print(city, details["literacy"])

# Population Density
def population_density():
    print("\nPopulation Density")

    for city, details in cities.items():
        density = details["population"] / details["area"]
        print(city, ":", round(density, 2))

# Highest Density City
def highest_density():
    highest = ""
    max_density = -1

    for city, details in cities.items():
        density = details["population"] / details["area"]

        if density > max_density:
            max_density = density
            highest = city

    print("Highest Density City:", highest, "-", round(max_density, 2))

# City Categories
def city_categories():
    print("\nCity Categories")

    for city, details in cities.items():

        pop = details["population"]

        if pop < 1000000:
            category = "Small"
        elif pop <= 5000000:
            category = "Medium"
        else:
            category = "Large"

        print(city, ":", category)

# Development Priority List
def development_priority():
    print("\nDevelopment Priority Cities")

    for city, details in cities.items():
        if details["literacy"] < 85:
            print(city)

# High Literacy Dictionary
def high_literacy_dict():
    high = {}

    for city, details in cities.items():
        if details["literacy"] >= 90:
            high[city] = details

    print("\nHigh Literacy Cities")
    print(high)

# Low Literacy Dictionary
def low_literacy_dict():
    low = {}

    for city, details in cities.items():
        if details["literacy"] < 85:
            low[city] = details

    print("\nLow Literacy Cities")
    print(low)

# National Summary Report
def national_report():
    most_populated()
    least_populated()
    average_population()
    highest_density()

# Menu Driven Program
while True:

    print("\n===== City Population Dashboard =====")
    print("1. Display All Cities")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Literacy Above 90%")
    print("6. Literacy Below Average")
    print("7. Population Density")
    print("8. Highest Density City")
    print("9. City Categories")
    print("10. Development Priority List")
    print("11. High Literacy Cities")
    print("12. Low Literacy Cities")
    print("13. National Summary Report")
    print("14. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_cities()
    elif choice == 2:
        most_populated()
    elif choice == 3:
        least_populated()
    elif choice == 4:
        average_population()
    elif choice == 5:
        high_literacy()
    elif choice == 6:
        literacy_below_average()
    elif choice == 7:
        population_density()
    elif choice == 8:
        highest_density()
    elif choice == 9:
        city_categories()
    elif choice == 10:
        development_priority()
    elif choice == 11:
        high_literacy_dict()
    elif choice == 12:
        low_literacy_dict()
    elif choice == 13:
        national_report()
    elif choice == 14:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")