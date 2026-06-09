# #String-Based Attendance Tracker
# '''_ _ _ ___ _ __ _ __ _ ___ __ _ _ __
# Write a program to:
# 1. Count Present and Absent days.
# 2. Calculate attendance percentage.
# 3. Find the longest consecutive streak of Presence.
# 4. Find the longest consecutive streak of Absence.
# 5. Determine whether attendance is below 75%.
# _ _ __ _ _ _ __ _ __ _ _ __ _ __ _ __ '''
# Attendance record
attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record")
print(attendance)

# Count present and absent days
present = attendance.count("P")
absent = attendance.count("A")

print("Present Days:", present)
print("Absent Days:", absent)

# Calculate attendance percentage
percentage = (present /len(attendance)) * 100

print("Attendance Percentage", percentage)

# Find longest present streak
max_present = 0
current_present = 0

for ch in attendance:

    if ch == "P":
        current_present += 1

        if current_present > max_present:
            max_present = current_present

    else:
        current_present = 0

print("Longest Present Streak:", max_present)

# Find longest absent streak
max_absent = 0
current_absent = 0

for ch in attendance:

    if ch == "A":
        current_absent += 1

        if current_absent > max_absent:
            max_absent = current_absent

    else:
        current_absent = 0

print("Longest Absent Streak:", max_absent)

# Check attendance status
if percentage < 75:
    print("Attendance Status: Below 75%")

else:
    print("Attendance Status: Above 75%")