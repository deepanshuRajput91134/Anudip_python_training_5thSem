# Bus Route Monitoring
'''_ _ _ _ _ _ _ _ __ _ _ _ _ _ _  _
• Find the busiest stop.
• Display stops with fewer than 10 passengers.
• Calculate average passengers.
• Determine whether any stop exceeded 25 passengers.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'''
# Bus Route Monitoring

passengers = [12, 18, 25, 30, 28, 15, 8]

# Busiest stop
highest = max(passengers)

print("Busiest Stop Passenger Count:", highest)

# Stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Average passengers
average = sum(passengers) / len(passengers)

print("\nAverage Passengers:", average)

# Check stops exceeding 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("\nA stop exceeded 25 passengers")
else:
    print("\nNo stop exceeded 25 passengers")