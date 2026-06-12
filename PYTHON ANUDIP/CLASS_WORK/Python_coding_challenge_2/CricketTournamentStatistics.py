#Cricket Tournament Statistics
'''_ _ _ __ __ ___ __ _ __ _ __ _ __ _ ___ 
1. Find the Orange Cap winner.
2. Find the lowest scorer.
3. Calculate total runs scored.
4. Display players scoring more than 500 runs.
5. Create a list of players scoring below 400.
 __ _ _ _ _. __ _ _ _ _ _ _ _ _ __ _ _'''
# Cricket Tournament Statistics

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

# 1. Find the Orange Cap winner
orange_cap = max(runs, key=runs.get)

print("Orange Cap Winner:")
print(orange_cap, "(", runs[orange_cap], "runs )")

# 2. Find the lowest scorer
lowest_scorer = min(runs, key=runs.get)

print("\nLowest Scorer:")
print(lowest_scorer, "(", runs[lowest_scorer], "runs )")

# 3. Calculate total runs scored
total_runs = sum(runs.values())

print("\nTotal Runs:", total_runs)

# 4. Display players scoring more than 500 runs
print("\nPlayers Scoring Above 500:")

for player, score in runs.items():
    if score > 500:
        print(player)

# 5. Create a list of players scoring below 400
below_400 = []

for player, score in runs.items():
    if score < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)