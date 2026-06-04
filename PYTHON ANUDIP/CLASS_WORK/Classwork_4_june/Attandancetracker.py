#A teacher is recording a student attandance the stringh of class is 30 ,everyime is need to insert student is present or absent,so count the total number of student present as well as absent
present = 0
absent = 0

student = 1

while student <= 30:

    print("Student", student)

    attendance = input("Attendance (Present/Absent): ")

    if attendance.lower() == "present":
        present += 1

    else:
        absent += 1

    student += 1

print("No. of Students Present:", present)
print("No. of Students Absent:", absent)