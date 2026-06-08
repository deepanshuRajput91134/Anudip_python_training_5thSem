#Product Price Analysis
'''_ _ _ _ __ _ _ __ _ _ _ __ _ _
• Display products costing more than ₹5000.
• Count products costing less than ₹3000.
• Find the most expensive product.
• Create a list of products priced between ₹2000 and ₹10000.
• Calculate the total value of all products.
_ _ _ _ __ _ _ __ _ _ __. _ __ _ _ __ _ '''
# Dictionary storing product prices
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Display products costing more than 5000
print("Products costing more than 5000:")

for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

# Count products costing less than 3000
count = 0

for price in prices.values():
    if price < 3000:
        count += 1

print("\nProducts costing less than 3000:", count)

# Find the most expensive product
highest = max(prices, key=prices.get)

print("\nMost expensive product:")
print(highest, ":", prices[highest])

# Create list of products priced between 2000 and 10000
middle_products = []

for product, price in prices.items():
    if 2000 <= price <= 10000:
        middle_products.append(product)

print("\nProducts priced between 2000 and 10000:")
print(middle_products)

# Calculate total value of all products
total = sum(prices.values())

print("\nTotal value of all products:", total)