# Mobile Screen Time Analyzer
'''_ __ _ __ _ _ _. __ _ _ __ _ _ _ __ _
1. Calculate average screen time.
2. Find the highest and lowest screen time.
3. Count days exceeding 200 minutes.
4. Display days with healthy usage (<180 minutes).
5. Categorize usage:
o Healthy (<180)
o Moderate (180–240)
o Excessive (>240)
  _ __ _ _ _ __ _ _ __ _ _ __ '''
# Mobile Screen Time Analyzer

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Calculate average screen time
average = sum(screen_time) / len(screen_time)
print("Average Screen Time:", average, "minutes")

# 2. Find highest and lowest screen time
highest = max(screen_time)
lowest = min(screen_time)

print("Highest Screen Time:", highest, "minutes")
print("Lowest Screen Time:", lowest, "minutes")

# 3. Count days exceeding 200 minutes
count = 0

for time in screen_time:
    if time > 200:
        count += 1

print("Days Exceeding 200 Minutes:", count)

# 4. Display days with healthy usage (<180)
print("\nHealthy Usage Days:")

for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i + 1)

# 5. Categorize usage
healthy = 0
moderate = 0
excessive = 0

for time in screen_time:

    if time < 180:
        healthy += 1

    elif time <= 240:
        moderate += 1

    else:
        excessive += 1

print("\nHealthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)