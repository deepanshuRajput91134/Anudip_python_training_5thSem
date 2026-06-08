# Student Marks Analysis

'''_. _ _ _ _ _ __ _ __ _ __ __ _       __ _
• Display students scoring 80 or above.
• Count the number of students who failed (marks < 40).
• Find the highest scorer.
• Create a list of students scoring between 60 and 75.
_ _. _ _ _ _ _. __ _ _ _ _ _. _. _ __ _ _ _ __ _'''

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Students scoring 80 or above
print("Students scoring 80 or above:")
for name, score in marks.items():
    if score >= 80:
        print(name, ":", score)

# Count failed students
failed = 0
for score in marks.values():
    if score < 40:
        failed += 1

print("\nNumber of failed students:", failed)

# Highest scorer
highest = max(marks, key=marks.get)
print("\nHighest scorer:", highest, "-", marks[highest])

# Students scoring between 60 and 75
between = []

for name, score in marks.items():
    if 60 <= score <= 75:
        between.append(name)

print("\nStudents scoring between 60 and 75:", between)

# Assign grades
print("\nGrades:")
for name, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(name, ":", grade)