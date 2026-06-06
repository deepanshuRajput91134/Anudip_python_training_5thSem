# Train Reservation Waiting List
'''_ _ _ _ _ _ _ _ _ _ _ _ _ ____ _ _ 
• Display all waiting-list passengers.
• Count confirmed and waiting passengers.
• Find whether a specific passenger has a confirmed ticket.
• Create separate lists for confirmed and waiting passengers.
_ _ _ _ _ _ _ __ _ _ __ _ _ _ _ _'''
# Train Reservation Waiting List

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Waiting list passengers
print("Waiting List Passengers:")

for p in passengers:
    if p[1] == "Waiting":
        print(p[0])

# Count confirmed and waiting passengers
confirmed = 0
waiting = 0

for p in passengers:
    if p[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("\nConfirmed Passengers:", confirmed)
print("Waiting Passengers:", waiting)

# Check specific passenger
search = "Priya"
found = False

for p in passengers:
    if p[0] == search and p[1] == "Confirmed":
        found = True
        break

if found:
    print("\nPassenger has confirmed ticket")
else:
    print("\nPassenger does not have confirmed ticket")

# Separate lists
confirmed_list = []
waiting_list = []

for p in passengers:
    if p[1] == "Confirmed":
        confirmed_list.append(p[0])
    else:
        waiting_list.append(p[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)