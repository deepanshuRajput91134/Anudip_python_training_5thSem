#Bus Route Passenger Analysis
'''_ _ _ _. _ _ _ __ _ _ _ __ _ _ _ 
• Display stops having more than 20 passengers.
• Count stops with fewer than 10 passengers.
• Find the busiest stop.
• Create a list of stops requiring an extra bus (passengers > 25).
• Calculate the average number of passengers.
_. _ _ __ _. __ __ __ _. _ _ __ _ __. _ _ _ _ '''
# Dictionary storing passenger data
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Display stops having more than 20 passengers
print("Stops having more than 20 passengers:")

for stop, people in passengers.items():
    if people > 20:
        print(stop, ":", people)

# Count stops with fewer than 10 passengers
count = 0

for people in passengers.values():
    if people < 10:
        count += 1

print("\nStops with fewer than 10 passengers:", count)

# Find busiest stop
busiest = max(passengers, key=passengers.get)

print("\nBusiest stop:")
print(busiest, ":", passengers[busiest])

# Create list of stops requiring extra bus
extra_bus = []

for stop, people in passengers.items():
    if people > 25:
        extra_bus.append(stop)

print("\nStops requiring extra bus:")
print(extra_bus)

# Calculate average passengers
average = sum(passengers.values()) / len(passengers)

print("\nAverage number of passengers:", average)