#Daily Expense Tracker and Report Generator
''' _ __ _ _ _ _ _. __ _ _ __ _ _ _ _
Develop a program to:
1. Display all expenses.
2. Calculate total expenditure.
3. Find the category with highest and lowest spending.
4. Display expenses greater than ₹800.
5. Add a new expense category.
6. Update an existing expense amount.
7. Generate a summary report in report.txt containing:
o Total Expenses
o Highest Expense Category
o Lowest Expense Category
o Categories spending more than ₹800
 _ __ _ __ _ __ _ _. __ __ __ __ _ _ __ _'''
import os

# File path
current_folder = os.path.dirname(os.path.abspath(__file__))
expense_file = os.path.join(current_folder, "expenses.txt")
report_file = os.path.join(current_folder, "report.txt")


# Read expenses from file
def read_expenses():

    expenses = []

    file = open(expense_file, "r")

    for line in file:

        data = line.strip().split(",")

        expense = {
            "category": data[0],
            "amount": int(data[1])
        }

        expenses.append(expense)

    file.close()

    return expenses


# Save expenses to file
def save_expenses(expenses):

    file = open(expense_file, "w")

    for expense in expenses:

        file.write(
            f"{expense['category']},{expense['amount']}\n"
        )

    file.close()


# Display all expenses
def display_expenses():

    expenses = read_expenses()

    print("\nExpense Records")
    print("-" * 40)

    for expense in expenses:

        print(
            expense["category"],
            expense["amount"]
        )


# Calculate total expenses
def total_expenses():

    expenses = read_expenses()

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print("Total Expenses =", total)


# Highest expense category
def highest_expense():

    expenses = read_expenses()

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:

            highest = expense

    print("\nHighest Expense Category")
    print(
        highest["category"],
        highest["amount"]
    )


# Lowest expense category
def lowest_expense():

    expenses = read_expenses()

    lowest = expenses[0]

    for expense in expenses:

        if expense["amount"] < lowest["amount"]:

            lowest = expense

    print("\nLowest Expense Category")
    print(
        lowest["category"],
        lowest["amount"]
    )


# Expenses above 800
def expenses_above_800():

    expenses = read_expenses()

    print("\nExpenses Greater Than 800")
    print("-" * 40)

    for expense in expenses:

        if expense["amount"] > 800:

            print(
                expense["category"],
                expense["amount"]
            )


# Add expense category
def add_expense():

    expenses = read_expenses()

    category = input("Enter Category Name: ")
    amount = int(input("Enter Amount: "))

    expenses.append({
        "category": category,
        "amount": amount
    })

    save_expenses(expenses)

    print("Expense Added Successfully")


# Update expense amount
def update_expense():

    expenses = read_expenses()

    category = input("Enter Category Name: ")

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            new_amount = int(
                input("Enter New Amount: ")
            )

            expense["amount"] = new_amount

            found = True

            break

    if found:

        save_expenses(expenses)

        print("Expense Updated Successfully")

    else:

        print("Category Not Found")


# Generate report
def generate_report():

    expenses = read_expenses()

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    above_800 = []

    for expense in expenses:

        total += expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

        if expense["amount"] > 800:
            above_800.append(expense)

    file = open(report_file, "w")

    file.write("DAILY EXPENSE REPORT\n")
    file.write("=" * 30 + "\n\n")

    file.write(f"Total Expenses : {total}\n\n")

    file.write(
        f"Highest Expense Category : "
        f"{highest['category']} "
        f"({highest['amount']})\n"
    )

    file.write(
        f"Lowest Expense Category : "
        f"{lowest['category']} "
        f"({lowest['amount']})\n\n"
    )

    file.write(
        "Categories Spending More Than 800\n"
    )

    file.write("-" * 30 + "\n")

    for expense in above_800:

        file.write(
            f"{expense['category']} "
            f"{expense['amount']}\n"
        )

    file.close()

    print("Report Generated Successfully")
    print("Data Saved In report.txt")


# Main Menu
while True:

    print("\n===== Daily Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenses")
    print("3. Highest Expense Category")
    print("4. Lowest Expense Category")
    print("5. Expenses Greater Than 800")
    print("6. Add Expense Category")
    print("7. Update Expense Amount")
    print("8. Generate Report")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_expenses()

    elif choice == 2:
        total_expenses()

    elif choice == 3:
        highest_expense()

    elif choice == 4:
        lowest_expense()

    elif choice == 5:
        expenses_above_800()

    elif choice == 6:
        add_expense()

    elif choice == 7:
        update_expense()

    elif choice == 8:
        generate_report()

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")