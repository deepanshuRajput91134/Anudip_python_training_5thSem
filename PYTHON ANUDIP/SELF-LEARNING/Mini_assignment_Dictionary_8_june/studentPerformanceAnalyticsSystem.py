#Student Performance Analytics System
'''_ _ ___ _ __ _ __________    __
1. Display all student records.
2. Search a student using Student ID.
3. Add a new student.
4. Update marks of an existing student.
5. Delete a student.
6. Find topper and lowest scorer.
7. Calculate class average.
8. Count pass and fail students.
9. Generate grades:
o A (90+)
o B (75–89)
o C (50–74)
o F (<50)
10. Display students scoring above average.
11. Display top 5 performers.
12. Create a separate dictionary for scholarship students (marks > 85).
_ _ _ _ __ _ __ _ _ __ _ _ _. _ '''
# ==========================================
# Student Performance Analytics System
# ==========================================

students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Neha", "marks": 67},
    "S105": {"name": "Amit", "marks": 45},
    "S106": {"name": "Riya", "marks": 88},
    "S107": {"name": "Karan", "marks": 55},
    "S108": {"name": "Pooja", "marks": 39},
    "S109": {"name": "Arjun", "marks": 95},
    "S110": {"name": "Simran", "marks": 81},
    "S111": {"name": "Vikas", "marks": 60},
    "S112": {"name": "Nisha", "marks": 49},
    "S113": {"name": "Rohit", "marks": 73},
    "S114": {"name": "Sneha", "marks": 92},
    "S115": {"name": "Deepak", "marks": 58},
    "S116": {"name": "Komal", "marks": 77},
    "S117": {"name": "Yash", "marks": 83},
    "S118": {"name": "Tina", "marks": 64},
    "S119": {"name": "Manoj", "marks": 38},
    "S120": {"name": "Kriti", "marks": 90},
    "S121": {"name": "Ramesh", "marks": 52},
    "S122": {"name": "Suman", "marks": 86},
    "S123": {"name": "Ajay", "marks": 41},
    "S124": {"name": "Meena", "marks": 96},
    "S125": {"name": "Varun", "marks": 69},
    "S126": {"name": "Aisha", "marks": 74},
    "S127": {"name": "Tarun", "marks": 47},
    "S128": {"name": "Payal", "marks": 89},
    "S129": {"name": "Nitin", "marks": 53},
    "S130": {"name": "Kavya", "marks": 98}
}

# ==========================================
# Function to Display All Students
# ==========================================

def display_students():
    print("\n------ Student Records ------")
    
    for sid, details in students.items():
        print(sid, " | ", details["name"], " | ", details["marks"])


# ==========================================
# Search Student by ID
# ==========================================

def search_student():
    sid = input("Enter Student ID: ")
    
    if sid in students:
        print("Student Found")
        print("Name :", students[sid]["name"])
        print("Marks:", students[sid]["marks"])
    else:
        print("Student Not Found")


# ==========================================
# Add New Student
# ==========================================

def add_student():
    sid = input("Enter Student ID: ")
    
    if sid in students:
        print("Student ID already exists")
    else:
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        
        students[sid] = {
            "name": name,
            "marks": marks
        }
        
        print("Student Added Successfully")


# ==========================================
# Update Marks
# ==========================================

def update_marks():
    sid = input("Enter Student ID: ")
    
    if sid in students:
        new_marks = int(input("Enter New Marks: "))
        students[sid]["marks"] = new_marks
        
        print("Marks Updated Successfully")
    else:
        print("Student Not Found")


# ==========================================
# Delete Student
# ==========================================

def delete_student():
    sid = input("Enter Student ID: ")
    
    if sid in students:
        del students[sid]
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")


# ==========================================
# Find Topper and Lowest Scorer
# ==========================================

def topper_lowest():
    topper = ""
    lowest = ""
    
    max_marks = -1
    min_marks = 101
    
    for sid, details in students.items():
        
        if details["marks"] > max_marks:
            max_marks = details["marks"]
            topper = details["name"]
        
        if details["marks"] < min_marks:
            min_marks = details["marks"]
            lowest = details["name"]
    
    print("\nTopper :", topper, "-", max_marks)
    print("Lowest Scorer :", lowest, "-", min_marks)


# ==========================================
# Calculate Average
# ==========================================

def class_average():
    total = 0
    
    for details in students.values():
        total = total + details["marks"]
    
    avg = total / len(students)
    
    print("Class Average =", avg)


# ==========================================
# Count Pass and Fail
# ==========================================

def pass_fail_count():
    passed = 0
    failed = 0
    
    for details in students.values():
        
        if details["marks"] >= 50:
            passed += 1
        else:
            failed += 1
    
    print("Passed Students :", passed)
    print("Failed Students :", failed)


# ==========================================
# Generate Grades
# ==========================================

def generate_grades():
    print("\n------ Grades ------")
    
    for sid, details in students.items():
        
        marks = details["marks"]
        
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "F"
        
        print(sid, "|", details["name"], "|", marks, "| Grade:", grade)


# ==========================================
# Students Above Average
# ==========================================

def above_average():
    total = 0
    
    for details in students.values():
        total += details["marks"]
    
    avg = total / len(students)
    
    print("\nStudents Above Average")
    
    for sid, details in students.items():
        
        if details["marks"] > avg:
            print(sid, "|", details["name"], "|", details["marks"])


# ==========================================
# Top 5 Performers (Without sort())
# ==========================================

def top_5_students():
    
    temp_students = students.copy()
    
    print("\n------ Top 5 Performers ------")
    
    for i in range(5):
        
        top_id = ""
        top_marks = -1
        
        for sid, details in temp_students.items():
            
            if details["marks"] > top_marks:
                top_marks = details["marks"]
                top_id = sid
        
        print(top_id, "|", temp_students[top_id]["name"], "|", top_marks)
        
        del temp_students[top_id]


# ==========================================
# Scholarship Students
# ==========================================

def scholarship_students():
    
    scholarship = {}
    
    for sid, details in students.items():
        
        if details["marks"] > 85:
            scholarship[sid] = details
    
    print("\n------ Scholarship Students ------")
    
    for sid, details in scholarship.items():
        print(sid, "|", details["name"], "|", details["marks"])


# ==========================================
# Menu Driven Program
# ==========================================

while True:
    
    print("\n========== MENU ==========")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper and Lowest")
    print("7. Calculate Average")
    print("8. Count Pass and Fail")
    print("9. Generate Grades")
    print("10. Students Above Average")
    print("11. Top 5 Performers")
    print("12. Scholarship Students")
    print("13. Exit")
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        display_students()
    
    elif choice == 2:
        search_student()
    
    elif choice == 3:
        add_student()
    
    elif choice == 4:
        update_marks()
    
    elif choice == 5:
        delete_student()
    
    elif choice == 6:
        topper_lowest()
    
    elif choice == 7:
        class_average()
    
    elif choice == 8:
        pass_fail_count()
    
    elif choice == 9:
        generate_grades()
    
    elif choice == 10:
        above_average()
    
    elif choice == 11:
        top_5_students()
    
    elif choice == 12:
        scholarship_students()
    
    elif choice == 13:
        print("Program Ended")
        break
    
    else:
        print("Invalid Choice")