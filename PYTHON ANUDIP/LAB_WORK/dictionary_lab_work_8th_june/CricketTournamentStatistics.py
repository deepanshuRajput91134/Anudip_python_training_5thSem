#Cricket Tournament Statistics
'''_ _. _ __ _ _ __ _ __ __. __ _ _ _ _ 
1. Display players scoring more than 500 runs.
2. Find the Orange Cap winner.
3. Find the lowest scorer.
4. Calculate total runs scored.
5. Create a list of players scoring below 400.
6. Count players scoring between 400 and 600 runs.
_. _ __. __ _ _ __ ___ __ _ _ _'''
# Dictionary storing tournament runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player, score in runs.items():
    if score > 500:
        print(player)

# Find Orange Cap winner
orange_cap = max(runs, key=runs.get)

print("\nOrange Cap Winner:")
print(orange_cap, "(", runs[orange_cap], ")")

# Find lowest scorer
lowest = min(runs, key=runs.get)

print("\nLowest Scorer:")
print(lowest, "(", runs[lowest], ")")

# Calculate total tournament runs
total = sum(runs.values())

print("\nTotal Tournament Runs:", total)

# Create list of players scoring below 400
below_400 = []

for player, score in runs.items():
    if score < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# Count players scoring between 400 and 600
count = 0

for score in runs.values():
    if 400 <= score <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)