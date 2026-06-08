# Dictionary storing cricket scores
'''_ _ _ ___ __ _ _ _ __ _ _ _
• Display players who scored 50 or more runs.
• Count the number of centuries.
• Find the player with the highest score.
• Create a list of players scoring below 30 runs.
• Determine how many players scored between 50 and 99.
_ _ _ _ _ _ _ _ _ _ _ __ __ _ ___ _'''
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Display players scoring 50 or more
print("Players scoring 50 or more:")

for player, runs in scores.items():
    if runs >= 50:
        print(player, ":", runs)

# Count number of centuries
centuries = 0

for runs in scores.values():
    if runs >= 100:
        centuries += 1

print("\nNumber of centuries:", centuries)

# Find player with highest score
highest = max(scores, key=scores.get)

print("\nHighest scorer:")
print(highest, ":", scores[highest])

# Create list of players scoring below 30
below_30 = []

for player, runs in scores.items():
    if runs < 30:
        below_30.append(player)

print("\nPlayers scoring below 30:")
print(below_30)

# Count players scoring between 50 and 99
count = 0

for runs in scores.values():
    if 50 <= runs <= 99:
        count += 1

print("\nPlayers scoring between 50 and 99:", count)