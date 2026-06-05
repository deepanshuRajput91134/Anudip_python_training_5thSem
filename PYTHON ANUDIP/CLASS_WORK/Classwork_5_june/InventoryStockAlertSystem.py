# Stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Variables and lists
out_of_stock = 0
available_products = 0

restock_required = []
healthy_stock = []

# Loop through stock list
for item in stock:

    # Count out of stock products
    if item == 0:
        out_of_stock += 1

    # Products needing restock
    if item < 10:
        restock_required.append(item)

    # Count available products
    if item > 0:
        available_products += 1

    # Healthy stock products
    if item >= 15:
        healthy_stock.append(item)

# Display output
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)