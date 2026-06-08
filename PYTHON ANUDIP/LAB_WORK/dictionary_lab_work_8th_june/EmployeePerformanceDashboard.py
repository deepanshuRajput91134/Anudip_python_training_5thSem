#Employee Performance Dashboard
'''_ _ _ _ _ __ __ _ __ __ _ _ _ __ 
1. Display employees scoring above 80.
2. Count employees needing improvement (score < 60).
3. Find the top performer.
4. Calculate average performance score.
5. Create separate lists:
o Excellent (≥ 90)
o Good (75–89)
o Average (60–74)
o Poor (< 60)
_ __ _ _ _. _ _ __ _ _ '''
# Dictionary storing employee performance
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Display employees scoring above 80
print("Employees Scoring Above 80:")

for emp, score in performance.items():
    if score > 80:
        print(emp)

# Count employees needing improvement
count = 0

for score in performance.values():
    if score < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# Find top performer
top = max(performance, key=performance.get)

print("\nTop Performer:")
print(top, "(", performance[top], ")")

# Calculate average score
average = sum(performance.values()) / len(performance)

print("\nAverage Score:", average)

# Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():

    # Excellent category
    if score >= 90:
        excellent.append(emp)

    # Good category
    elif 75 <= score <= 89:
        good.append(emp)

    # Average category
    elif 60 <= score <= 74:
        average_list.append(emp)

    # Poor category
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)