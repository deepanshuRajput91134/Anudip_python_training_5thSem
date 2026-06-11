#Employee Payroll Management System 
'''_ _ _ _ _ _ _ _ __ _ __ _ _ _ _ _ 
Create a menu-driven program to:
1. Display all employee records.
2. Search employee details using Employee ID.
3. Calculate the average salary.
4. Find the highest-paid and lowest-paid employee.
5. Display employees earning above ₹50,000.
6. Add a new employee record to the file.
7. Generate salary categories:
o High (₹60,000 and above)
o Medium (₹40,000–₹59,999)
o Low (Below ₹40,000)
_ _ _ _ _ _ _ __. __ _ _ _ __ _ _ _ __ _ _'''
# Employee Payroll Management System

# Function to read employee data from file
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "employees.txt")

def read_employees():
    employees = []

    file = open(file_path, "r")
    for line in file:
        data = line.strip().split(",")

        employee = {
            "id": data[0],
            "name": data[1],
            "salary": int(data[2])
        }

        employees.append(employee)

    file.close()

    return employees


# Function to display all employees
def display_employees():
    employees = read_employees()

    print("\nEmployee Records")
    print("-" * 40)

    for emp in employees:
        print(emp["id"], emp["name"], emp["salary"])


# Function to search employee by ID
def search_employee():
    employees = read_employees()

    emp_id = input("Enter Employee ID: ")

    found = False

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Salary:", emp["salary"])

            found = True
            break

    if found == False:
        print("Employee Not Found")


# Function to calculate average salary
def average_salary():
    employees = read_employees()

    total = 0

    for emp in employees:
        total += emp["salary"]

    average = total / len(employees)

    print("Average Salary =", average)


# Function to find highest paid employee
def highest_paid():
    employees = read_employees()

    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print("\nHighest Paid Employee")
    print(highest["id"], highest["name"], highest["salary"])


# Function to find lowest paid employee
def lowest_paid():
    employees = read_employees()

    lowest = employees[0]

    for emp in employees:
        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print("\nLowest Paid Employee")
    print(lowest["id"], lowest["name"], lowest["salary"])


# Function to display employees earning above 50000
def salary_above_50000():
    employees = read_employees()

    print("\nEmployees Earning Above 50000")
    print("-" * 40)

    for emp in employees:
        if emp["salary"] > 50000:
            print(emp["id"], emp["name"], emp["salary"])


# Function to add new employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open(file_path, "a")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Added Successfully")


# Function to generate salary categories
def salary_categories():
    employees = read_employees()

    print("\nSalary Categories")
    print("-" * 40)

    for emp in employees:

        if emp["salary"] >= 60000:
            category = "High"

        elif emp["salary"] >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(
            emp["id"],
            emp["name"],
            emp["salary"],
            "Category:",
            category
        )


# Main Menu
while True:

    print("\n")
    print("===== Employee Payroll Management =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Calculate Average Salary")
    print("4. Highest Paid Employee")
    print("5. Lowest Paid Employee")
    print("6. Employees Earning Above 50000")
    print("7. Add New Employee")
    print("8. Salary Categories")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_employees()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_paid()

    elif choice == 5:
        lowest_paid()

    elif choice == 6:
        salary_above_50000()

    elif choice == 7:
        add_employee()

    elif choice == 8:
        salary_categories()

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")