# Inventory Management System
'''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
• Display products with stock less than 10.
• Count products having stock more than 50.
• Find the product with the minimum stock.
• Create a list of products that require restocking (stock < 20).
• Calculate the total inventory count.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'''
# Dictionary storing product stock
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock less than 10
print("Products with stock less than 10:")

for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# Count products having stock more than 50
count = 0

for stock in inventory.values():
    if stock > 50:
        count += 1

print("\nProducts with stock more than 50:", count)

# Find product with minimum stock
minimum = min(inventory, key=inventory.get)

print("\nProduct with minimum stock:")
print(minimum, ":", inventory[minimum])

# Create list of products requiring restocking
restock = []

for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)

print("\nProducts requiring restocking:")
print(restock)

# Calculate total inventory count
total = sum(inventory.values())

print("\nTotal inventory count:", total)
