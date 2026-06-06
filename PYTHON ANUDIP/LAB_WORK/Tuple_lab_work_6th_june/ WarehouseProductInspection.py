# Warehouse Product Inspection
''' _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _
• Display failed product IDs.
• Count passed and failed products.
• Calculate pass percentage.
• Stop checking if 3 failures are found.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'''
# Warehouse Product Inspection

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

print("Failed Product IDs:")

for product in products:

    if product[1] == "Fail":
        print(product[0])
        fail_count += 1

    else:
        pass_count += 1

# Pass percentage
percentage = (pass_count / len(products)) * 100

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)

print("\nPass Percentage:", percentage)

# Stop checking after 3 failures
failure = 0

for product in products:

    if product[1] == "Fail":
        failure += 1

    if failure == 3:
        print("\n3 Failures Found")
        break