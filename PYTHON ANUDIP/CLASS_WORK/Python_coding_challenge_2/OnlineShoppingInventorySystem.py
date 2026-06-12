# Online Shopping Inventory System
'''__ _ __ _ __ _ __ __ _ __ __ __ _ 
1. Display products with stock below 15 units.
2. Find the product with maximum stock.
3. Find the product with minimum stock.
4. Calculate total stock available.
5. Create a list of products requiring restocking (<10 units).
_ _ ___ _ _ __ _ _ _ _ __ _ _ __ _ __ __ _'''
# Online Shopping Inventory System

inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products with stock below 15 units
print("Products with Stock Below 15:")

for product, stock in inventory.items():
    if stock < 15:
        print(product)

# 2. Find the product with maximum stock
highest_product = max(inventory, key=inventory.get)

print("\nHighest Stock Product:")
print(highest_product, "(", inventory[highest_product], "units )")

# 3. Find the product with minimum stock
lowest_product = min(inventory, key=inventory.get)

print("\nLowest Stock Product:")
print(lowest_product, "(", inventory[lowest_product], "units )")

# 4. Calculate total stock available
total_stock = sum(inventory.values())

print("\nTotal Stock Available:", total_stock)

# 5. Create a list of products requiring restocking
restocking = []

for product, stock in inventory.items():
    if stock < 10:
        restocking.append(product)

print("\nProducts Requiring Restocking:")
print(restocking)