#Online Shopping Order Analytics
'''__ _ _ _ __ _ _ __ _ _ __
1. Display products sold more than 20 times.
2. Find the best-selling product.
3. Find the least-selling product.
4. Calculate total products sold.
5. Create a list of products requiring promotion (sales < 15).
6. Count products having sales between 10 and 30.
 _ __ _ _ _ _ _ _ __ _ _ _. __ _. __ _ _ _ '''
 # Dictionary storing product sales data
sales = {
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

# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")

for product, quantity in sales.items():
    if quantity > 20:
        print(product)

# Find best-selling product
best = max(sales, key=sales.get)

print("\nBest Selling Product:")
print(best, "(", sales[best], ")")

# Find least-selling product
least = min(sales, key=sales.get)

print("\nLeast Selling Product:")
print(least, "(", sales[least], ")")

# Calculate total products sold
total = sum(sales.values())

print("\nTotal Units Sold:", total)

# Create list of products requiring promotion
promotion = []

for product, quantity in sales.items():
    if quantity < 15:
        promotion.append(product)

print("\nProducts Requiring Promotion:")
print(promotion)

# Count products having sales between 10 and 30
count = 0

for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)