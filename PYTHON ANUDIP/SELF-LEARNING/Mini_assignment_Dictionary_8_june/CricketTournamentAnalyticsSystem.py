#Cricket Tournament Analytics System
'''_ _ _ _ __ _ _ ___ _. __ __ _ __
1. Add a book.
2. Remove a book.
3. Search a book by ID.
4. Search by title.
5. Update available copies.
6. Issue a book.
7. Return a book.
8. Display books with fewer than 3 copies.
9. Display books that are unavailable.
10. Find the most available book.
11. Generate a restocking report.
12. Create a separate dictionary of books requiring immediate purchase.
_.  __ __. _ _ _ __ _ _ _ __ _ _ _ _ __ _ _ _. _ __ _ _ _ '''
# ==========================================
# Cricket Tournament Analytics System
# ==========================================

players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 580, "matches": 12, "wickets": 1},
    "Gill": {"runs": 520, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 350, "matches": 10, "wickets": 8},
    "Jadeja": {"runs": 310, "matches": 12, "wickets": 15},
    "Bumrah": {"runs": 45, "matches": 12, "wickets": 22},
    "Shami": {"runs": 30, "matches": 11, "wickets": 20},
    "Siraj": {"runs": 25, "matches": 12, "wickets": 18},
    "KL Rahul": {"runs": 410, "matches": 10, "wickets": 0},
    "Surya": {"runs": 390, "matches": 11, "wickets": 1},
    "Player11": {"runs": 280, "matches": 10, "wickets": 4},
    "Player12": {"runs": 460, "matches": 11, "wickets": 2},
    "Player13": {"runs": 190, "matches": 9, "wickets": 6},
    "Player14": {"runs": 510, "matches": 12, "wickets": 3},
    "Player15": {"runs": 340, "matches": 10, "wickets": 9},
    "Player16": {"runs": 220, "matches": 8, "wickets": 11},
    "Player17": {"runs": 600, "matches": 12, "wickets": 0},
    "Player18": {"runs": 145, "matches": 7, "wickets": 12},
    "Player19": {"runs": 275, "matches": 10, "wickets": 7},
    "Player20": {"runs": 380, "matches": 11, "wickets": 5},
    "Player21": {"runs": 495, "matches": 12, "wickets": 1},
    "Player22": {"runs": 160, "matches": 8, "wickets": 13},
    "Player23": {"runs": 325, "matches": 10, "wickets": 8},
    "Player24": {"runs": 415, "matches": 11, "wickets": 2},
    "Player25": {"runs": 210, "matches": 9, "wickets": 10},
    "Player26": {"runs": 540, "matches": 12, "wickets": 0},
    "Player27": {"runs": 300, "matches": 10, "wickets": 6},
    "Player28": {"runs": 180, "matches": 8, "wickets": 14},
    "Player29": {"runs": 450, "matches": 11, "wickets": 3},
    "Player30": {"runs": 260, "matches": 9, "wickets": 7}
}

# Display All Players
def display_players():
    for player, details in players.items():
        print(player, details)

# Highest Run Scorer
def highest_run_scorer():
    highest = ""
    max_runs = -1

    for player, details in players.items():
        if details["runs"] > max_runs:
            max_runs = details["runs"]
            highest = player

    print("Highest Run Scorer:", highest, "-", max_runs)

# Lowest Run Scorer
def lowest_run_scorer():
    lowest = ""
    min_runs = 999999

    for player, details in players.items():
        if details["runs"] < min_runs:
            min_runs = details["runs"]
            lowest = player

    print("Lowest Run Scorer:", lowest, "-", min_runs)

# Average Runs
def average_runs():
    total = 0

    for details in players.values():
        total += details["runs"]

    avg = total / len(players)

    print("Average Runs =", avg)

# Maximum Wickets
def max_wickets():
    best = ""
    max_wicket = -1

    for player, details in players.items():
        if details["wickets"] > max_wicket:
            max_wicket = details["wickets"]
            best = player

    print("Maximum Wickets:", best, "-", max_wicket)

# All Rounders
def all_rounders():
    print("\nAll Rounders")

    for player, details in players.items():
        if details["runs"] > 300 and details["wickets"] > 5:
            print(player, details)

# Players Above Average
def above_average():
    total = 0

    for details in players.values():
        total += details["runs"]

    avg = total / len(players)

    print("\nPlayers Above Average")

    for player, details in players.items():
        if details["runs"] > avg:
            print(player, details["runs"])

# Player Categories
def categories():
    print("\nPlayer Categories")

    for player, details in players.items():

        runs = details["runs"]

        if runs >= 500:
            category = "Star Performer"
        elif runs >= 350:
            category = "Good Performer"
        elif runs >= 200:
            category = "Average Performer"
        else:
            category = "Poor Performer"

        print(player, ":", category)

# Team Statistics
def team_statistics():
    total_runs = 0
    total_wickets = 0

    for details in players.values():
        total_runs += details["runs"]
        total_wickets += details["wickets"]

    print("Total Runs:", total_runs)
    print("Total Wickets:", total_wickets)

# Top 5 Batsmen
def top_5_batsmen():
    temp = players.copy()

    print("\nTop 5 Batsmen")

    for i in range(5):

        best_player = ""
        max_runs = -1

        for player, details in temp.items():
            if details["runs"] > max_runs:
                max_runs = details["runs"]
                best_player = player

        print(best_player, "-", max_runs)
        del temp[best_player]

# Top 5 Bowlers
def top_5_bowlers():
    temp = players.copy()

    print("\nTop 5 Bowlers")

    for i in range(5):

        best_player = ""
        max_wickets = -1

        for player, details in temp.items():
            if details["wickets"] > max_wickets:
                max_wickets = details["wickets"]
                best_player = player

        print(best_player, "-", max_wickets)
        del temp[best_player]

# Award Winners
def award_winners():

    highest_runs_player = ""
    highest_runs = -1

    highest_wicket_player = ""
    highest_wickets = -1

    for player, details in players.items():

        if details["runs"] > highest_runs:
            highest_runs = details["runs"]
            highest_runs_player = player

        if details["wickets"] > highest_wickets:
            highest_wickets = details["wickets"]
            highest_wicket_player = player

    awards = {
        "Best Batsman": highest_runs_player,
        "Best Bowler": highest_wicket_player
    }

    print("\nAward Winners")

    for award, winner in awards.items():
        print(award, ":", winner)

# Tournament Report
def tournament_report():
    highest_run_scorer()
    lowest_run_scorer()
    max_wickets()
    team_statistics()

# Menu Driven Program
while True:

    print("\n===== Cricket Tournament Analytics =====")
    print("1. Display All Players")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Average Runs")
    print("5. Maximum Wickets")
    print("6. All Rounders")
    print("7. Players Above Average")
    print("8. Player Categories")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Tournament Report")
    print("14. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_players()
    elif choice == 2:
        highest_run_scorer()
    elif choice == 3:
        lowest_run_scorer()
    elif choice == 4:
        average_runs()
    elif choice == 5:
        max_wickets()
    elif choice == 6:
        all_rounders()
    elif choice == 7:
        above_average()
    elif choice == 8:
        categories()
    elif choice == 9:
        team_statistics()
    elif choice == 10:
        top_5_batsmen()
    elif choice == 11:
        top_5_bowlers()
    elif choice == 12:
        award_winners()
    elif choice == 13:
        tournament_report()
    elif choice == 14:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")