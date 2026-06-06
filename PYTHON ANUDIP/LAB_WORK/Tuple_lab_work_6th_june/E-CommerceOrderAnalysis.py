# E-Commerce Order Analysis

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Products costing more than 1000
print("Products costing more than 1000:")

for item in orders:
    if item[1] > 1000:
        print(item[0], item[1])

# Most expensive product
highest = orders[0]

for item in orders:
    if item[1] > highest[1]:
        highest = item

print("\nMost Expensive Product:")
print(highest)

# Total order value
total = 0

for item in orders:
    total += item[1]

print("\nTotal Order Value:", total)

# Count products below 1000
count = 0

for item in orders:
    if item[1] < 1000:
        count += 1

print("\nProducts below 1000:", count)