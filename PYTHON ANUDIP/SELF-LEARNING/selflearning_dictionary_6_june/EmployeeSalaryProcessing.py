#Employee Salary Processing
'''_ _ _ _ _ _ __ _ _ __ _ _ _ __ _ __ 
• Display employees earning above ₹60,000.
• Count employees earning below ₹40,000.
• Find the highest-paid employee.
• Create a list of employees eligible for a bonus (salary > ₹50,000).
• Calculate the average salary.
_ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ __ _ '''
# Dictionary storing employee salary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Display employees earning above 60000
print("Employees earning above 60000:")

for emp, sal in salary.items():
    if sal > 60000:
        print(emp, ":", sal)

# Count employees earning below 40000
count = 0

for sal in salary.values():
    if sal < 40000:
        count += 1

print("\nEmployees earning below 40000:", count)

# Find highest-paid employee
highest = max(salary, key=salary.get)

print("\nHighest-paid employee:")
print(highest, ":", salary[highest])

# Create list of employees eligible for bonus
bonus = []

for emp, sal in salary.items():
    if sal > 50000:
        bonus.append(emp)

print("\nEmployees eligible for bonus:")
print(bonus)

# Calculate average salary
average = sum(salary.values()) / len(salary)

print("\nAverage salary:", average)