#Student Result Processing System
'''_ _ _ _ _ _ _ _ __ _ __ _ _ _ _
Write a program to:
1. Display all student records.
2. Search a student using Student ID.
3. Find topper and lowest scorer.
4. Calculate class average.
5. Count pass and fail students.
6. Generate grades:
o A (90+)
o B (75–89)
o C (40–74)
o F (<40)
7. Write grade reports into a new file named grades.txt.
_ __ _ _ _ _ _ __ __ _ _ __ _ _ __ __ _ '''
import os

# File path
current_folder = os.path.dirname(os.path.abspath(__file__))
result_file = os.path.join(current_folder, "results.txt")
grade_file = os.path.join(current_folder, "grades.txt")


# Read student records
def read_students():
    students = []

    file = open(result_file, "r")

    for line in file:
        data = line.strip().split(",")

        student = {
            "id": data[0],
            "name": data[1],
            "marks": int(data[2])
        }

        students.append(student)

    file.close()

    return students


# Display all students
def display_students():
    students = read_students()

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(
            student["id"],
            student["name"],
            student["marks"]
        )


# Search student
def search_student():
    students = read_students()

    student_id = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")
            print("ID :", student["id"])
            print("Name :", student["name"])
            print("Marks :", student["marks"])

            found = True
            break

    if not found:
        print("Student Not Found")


# Find topper
def find_topper():
    students = read_students()

    topper = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

    print("\nTopper")
    print(
        topper["id"],
        topper["name"],
        topper["marks"]
    )


# Find lowest scorer
def lowest_scorer():
    students = read_students()

    lowest = students[0]

    for student in students:

        if student["marks"] < lowest["marks"]:
            lowest = student

    print("\nLowest Scorer")
    print(
        lowest["id"],
        lowest["name"],
        lowest["marks"]
    )


# Calculate average
def class_average():
    students = read_students()

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Class Average =", average)


# Pass fail count
def pass_fail_count():
    students = read_students()

    passed = 0
    failed = 0

    for student in students:

        if student["marks"] >= 40:
            passed += 1
        else:
            failed += 1

    print("Passed Students :", passed)
    print("Failed Students :", failed)


# Generate grades
def generate_grades():

    students = read_students()

    print("\nGrade Report")
    print("-" * 50)

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(
            student["id"],
            student["name"],
            marks,
            "Grade:",
            grade
        )


# Write grades to grades.txt
def write_grade_report():

    students = read_students()

    file = open(grade_file, "w")

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        file.write(
            f"{student['id']},{student['name']},{marks},{grade}\n"
        )

    file.close()

    print("Grade report generated successfully.")
    print("Data saved in grades.txt")


# Main Menu
while True:

    print("\n===== Student Result Processing System =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Find Topper")
    print("4. Find Lowest Scorer")
    print("5. Calculate Class Average")
    print("6. Pass / Fail Count")
    print("7. Generate Grades")
    print("8. Write Grade Report")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        find_topper()

    elif choice == 4:
        lowest_scorer()

    elif choice == 5:
        class_average()

    elif choice == 6:
        pass_fail_count()

    elif choice == 7:
        generate_grades()

    elif choice == 8:
        write_grade_report()

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")