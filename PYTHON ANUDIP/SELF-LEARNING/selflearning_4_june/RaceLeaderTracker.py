n = int(input("Enter number of racers: "))

times = []

for i in range(n):
    lap = int(input(f"Enter lap time of racer {i+1}: "))
    times.append(lap)

fastest = min(times)
slowest = max(times)

print("Fastest Racer Position:", times.index(fastest) + 1)
print("Slowest Racer Position:", times.index(slowest) + 1)
print("Difference:", slowest - fastest)