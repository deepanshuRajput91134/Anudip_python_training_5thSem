#Online Quiz Performance
'''_ _ _ _ __ _ _ __ _ __ _ _ __ _ _
• Display students scoring 15 or above.
• Count students scoring below 10.
• Find the top performer.
• Create a list of students who passed (≥ 10 marks).
• Calculate the class average.
_ _ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _'''
# Dictionary storing quiz scores
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")

for student, marks in quiz_scores.items():
    if marks >= 15:
        print(student, ":", marks)

# Count students scoring below 10
count = 0

for marks in quiz_scores.values():
    if marks < 10:
        count += 1

print("\nStudents scoring below 10:", count)

# Find top performer
top = max(quiz_scores, key=quiz_scores.get)

print("\nTop performer:")
print(top, ":", quiz_scores[top])

# Create list of passed students
passed = []

for student, marks in quiz_scores.items():
    if marks >= 10:
        passed.append(student)

print("\nPassed students:")
print(passed)

# Calculate class average
average = sum(quiz_scores.values()) / len(quiz_scores)

print("\nClass average:", average)