#Employee Salary Report Generator
'''_ ___ _ _ __ _ _ _ __ _ _ __ _ _ __ 
1. Display employees earning more than ₹50,000.
2. Find the highest-paid employee.
3. Find the lowest-paid employee.
4. Calculate the average salary.
5. Generate salary categories:
o High (≥ ₹60,000)
o Medium (₹40,000 – ₹59,999)
o Low (< ₹40,000)
__ _ _ _ _ _ _ __ _ _ __ _ ___ ___ _ __ '''
# Employee Salary Report Generator

import os

def salary_report():
    try:
        file_path = os.path.join(
            os.path.dirname(__file__),
            "employees.txt"
        )

        employees = []

        with open(file_path, "r") as file:
            for line in file:
                emp_id, name, salary = line.strip().split(",")
                employees.append((emp_id, name, int(salary)))

        # Employees earning above 50000
        high_earners = []

        for emp in employees:
            if emp[2] > 50000:
                high_earners.append(emp[1])

        # Highest paid employee
        highest_paid = max(employees, key=lambda x: x[2])

        # Lowest paid employee
        lowest_paid = min(employees, key=lambda x: x[2])

        # Average salary
        total_salary = 0

        for emp in employees:
            total_salary += emp[2]

        average_salary = total_salary / len(employees)

        # Salary categories
        high_salary = []
        medium_salary = []
        low_salary = []

        for emp in employees:
            name = emp[1]
            salary = emp[2]

            if salary >= 60000:
                high_salary.append(name)
            elif salary >= 40000:
                medium_salary.append(name)
            else:
                low_salary.append(name)

        # Output
        print("Employees Earning Above ₹50,000:")
        for name in high_earners:
            print(name)

        print("\nHighest Paid Employee:")
        print(f"{highest_paid[1]} (₹{highest_paid[2]})")

        print("\nLowest Paid Employee:")
        print(f"{lowest_paid[1]} (₹{lowest_paid[2]})")

        print(f"\nAverage Salary: ₹{average_salary:.0f}")

        print("\nHigh Salary:")
        print(high_salary)

        print("\nMedium Salary:")
        print(medium_salary)

        print("\nLow Salary:")
        print(low_salary)

    except FileNotFoundError:
        print("Error: employees.txt file not found.")

    except Exception as e:
        print("An error occurred:", e)


salary_report()