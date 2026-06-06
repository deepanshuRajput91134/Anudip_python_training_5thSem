# Employee Salary Processing
'''_. _ _ _ _ _. _ _ _ _ _ _ _ _ _ _ _
• Display employees earning above ₹50,000.
• Find the highest-paid employee.
• Calculate total salary expenditure.
• Count employees earning below ₹40,000.
_ _ _. _ _ ___ _ _ _ _ _ _ _ _ _ _ _ _'''
# Employee Salary Processing

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Employees earning above 50000
print("Employees earning above 50000:")

for emp in employees:
    if emp[1] > 50000:
        print(emp)

# Highest paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("\nHighest Paid Employee:")
print(highest)

# Total salary expenditure
total = 0

for emp in employees:
    total += emp[1]

print("\nTotal Salary Expenditure:", total)

# Employees earning below 40000
count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("\nEmployees earning below 40000:", count)