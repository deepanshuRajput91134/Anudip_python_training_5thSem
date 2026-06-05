# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Empty lists and variables
passed = []
merit_list = []
failed_count = 0

# Assume first value as highest and lowest
highest = marks[0]
lowest = marks[0]

# Loop through all marks
for mark in marks:

    # Check passed students
    if mark >= 40:
        passed.append(mark)

    # Count failed students
    else:
        failed_count += 1

    # Find highest marks
    if mark > highest:
        highest = mark

    # Find lowest marks
    if mark < lowest:
        lowest = mark

    # Create merit list
    if mark > 75:
        merit_list.append(mark)

# Display output
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)