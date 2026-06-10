#E-Commerce Inventory & Sales Dashboard
'''_. _ _ _ _ _ _ _ _ _ _ _. _ _ _ 
1. Display all products.
2. Add a new product.
3. Update stock after sales.
4. Find out-of-stock products.
5. Find products with stock less than 5.
6. Calculate total inventory value.
7. Find best-selling product.
8. Find least-selling product.
9. Calculate total revenue generated.
10. Generate a low-stock report.
11. Display products whose sales exceed the average sales.
12. Create a dictionary of products eligible for promotion (sales < 10).
_ _ _ _ __ _ _ _. __ _ _ __ _. __ _ __ _ __ _ '''
# ==========================================
# E-Commerce Inventory & Sales Dashboard
# ==========================================

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 500, "stock": 20, "sold": 50},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 15, "sold": 30},
    "P104": {"name": "Monitor", "price": 12000, "stock": 8, "sold": 18},
    "P105": {"name": "Printer", "price": 8000, "stock": 4, "sold": 12},
    "P106": {"name": "Speaker", "price": 2500, "stock": 10, "sold": 22},
    "P107": {"name": "Webcam", "price": 1800, "stock": 3, "sold": 9},
    "P108": {"name": "Pendrive", "price": 700, "stock": 25, "sold": 40},
    "P109": {"name": "Hard Disk", "price": 4500, "stock": 7, "sold": 14},
    "P110": {"name": "Router", "price": 2000, "stock": 6, "sold": 11},
    "P111": {"name": "SSD", "price": 5000, "stock": 9, "sold": 17},
    "P112": {"name": "RAM", "price": 3500, "stock": 5, "sold": 19},
    "P113": {"name": "Power Bank", "price": 1500, "stock": 13, "sold": 27},
    "P114": {"name": "Charger", "price": 900, "stock": 2, "sold": 8},
    "P115": {"name": "Cable", "price": 300, "stock": 30, "sold": 60},
    "P116": {"name": "Tablet", "price": 25000, "stock": 5, "sold": 10},
    "P117": {"name": "Smart Watch", "price": 7000, "stock": 6, "sold": 15},
    "P118": {"name": "Phone", "price": 30000, "stock": 11, "sold": 35},
    "P119": {"name": "Headphones", "price": 2200, "stock": 4, "sold": 13},
    "P120": {"name": "Microphone", "price": 2800, "stock": 8, "sold": 16},
    "P121": {"name": "Camera", "price": 45000, "stock": 3, "sold": 7},
    "P122": {"name": "Projector", "price": 35000, "stock": 2, "sold": 5},
    "P123": {"name": "Scanner", "price": 6500, "stock": 4, "sold": 9},
    "P124": {"name": "TV", "price": 50000, "stock": 5, "sold": 12},
    "P125": {"name": "AC", "price": 40000, "stock": 2, "sold": 6},
    "P126": {"name": "Fan", "price": 2500, "stock": 10, "sold": 20},
    "P127": {"name": "Cooler", "price": 6000, "stock": 3, "sold": 8},
    "P128": {"name": "Mixer", "price": 3500, "stock": 7, "sold": 14},
    "P129": {"name": "Iron", "price": 1800, "stock": 6, "sold": 11},
    "P130": {"name": "Vacuum Cleaner", "price": 9000, "stock": 4, "sold": 9}
}

# Display Products
def display_products():
    for pid, details in products.items():
        print(pid, details)

# Add Product
def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = int(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    sold = int(input("Enter Sold Quantity: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

    print("Product Added Successfully")

# Update Stock After Sale
def update_stock():
    pid = input("Enter Product ID: ")

    if pid in products:
        qty = int(input("Enter Sold Quantity: "))

        if qty <= products[pid]["stock"]:
            products[pid]["stock"] -= qty
            products[pid]["sold"] += qty
            print("Stock Updated")
        else:
            print("Insufficient Stock")
    else:
        print("Product Not Found")

# Out of Stock Products
def out_of_stock():
    print("\nOut Of Stock Products")
    for pid, details in products.items():
        if details["stock"] == 0:
            print(pid, details["name"])

# Low Stock Products
def low_stock():
    print("\nProducts With Stock Less Than 5")
    for pid, details in products.items():
        if details["stock"] < 5:
            print(pid, details["name"], details["stock"])

# Total Inventory Value
def inventory_value():
    total = 0

    for details in products.values():
        total += details["price"] * details["stock"]

    print("Total Inventory Value =", total)

# Best Selling Product
def best_selling():
    best = ""
    max_sales = -1

    for pid, details in products.items():
        if details["sold"] > max_sales:
            max_sales = details["sold"]
            best = pid

    print("Best Selling Product:")
    print(best, products[best]["name"], max_sales)

# Least Selling Product
def least_selling():
    least = ""
    min_sales = 999999

    for pid, details in products.items():
        if details["sold"] < min_sales:
            min_sales = details["sold"]
            least = pid

    print("Least Selling Product:")
    print(least, products[least]["name"], min_sales)

# Total Revenue
def total_revenue():
    revenue = 0

    for details in products.values():
        revenue += details["price"] * details["sold"]

    print("Total Revenue =", revenue)

# Low Stock Report
def low_stock_report():
    print("\nLow Stock Report")
    for pid, details in products.items():
        if details["stock"] < 5:
            print(pid, details["name"], details["stock"])

# Above Average Sales
def above_average_sales():
    total_sales = 0

    for details in products.values():
        total_sales += details["sold"]

    avg = total_sales / len(products)

    print("\nProducts Above Average Sales")

    for pid, details in products.items():
        if details["sold"] > avg:
            print(pid, details["name"], details["sold"])

# Promotion Products
def promotion_products():
    promotion = {}

    for pid, details in products.items():
        if details["sold"] < 10:
            promotion[pid] = details

    print("\nPromotion Eligible Products")

    for pid, details in promotion.items():
        print(pid, details["name"], details["sold"])

# Business Report
def business_report():
    inventory_value()
    total_revenue()
    best_selling()
    least_selling()

# Menu
while True:

    print("\n===== E-Commerce Dashboard =====")
    print("1. Display Products")
    print("2. Add Product")
    print("3. Update Stock After Sale")
    print("4. Out Of Stock Products")
    print("5. Low Stock Products")
    print("6. Total Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Total Revenue")
    print("10. Low Stock Report")
    print("11. Above Average Sales")
    print("12. Promotion Products")
    print("13. Business Report")
    print("14. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_products()
    elif choice == 2:
        add_product()
    elif choice == 3:
        update_stock()
    elif choice == 4:
        out_of_stock()
    elif choice == 5:
        low_stock()
    elif choice == 6:
        inventory_value()
    elif choice == 7:
        best_selling()
    elif choice == 8:
        least_selling()
    elif choice == 9:
        total_revenue()
    elif choice == 10:
        low_stock_report()
    elif choice == 11:
        above_average_sales()
    elif choice == 12:
        promotion_products()
    elif choice == 13:
        business_report()
    elif choice == 14:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")