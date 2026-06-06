# Student Attendance Tracker
'''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
• Count present and absent days.
• Calculate attendance percentage.
• Determine eligibility (minimum 75% attendance).
• Display positions where the student was absent.
_ _ _. _ _ _ _ _ _ _ _ _ _'''
# Student Attendance Tracker

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = attendance.count('P')
absent = attendance.count('A')

print("Present Days:", present)
print("Absent Days:", absent)

# Attendance percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage)

# Eligibility check
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Absent positions
print("\nAbsent Positions:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)