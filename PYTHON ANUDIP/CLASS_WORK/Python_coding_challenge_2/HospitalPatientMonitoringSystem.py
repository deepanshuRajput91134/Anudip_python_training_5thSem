# #Hospital Patient Monitoring System
# '''_ _ __ _ _ _ _ _ __ _ _ __ _ _ _ __
# 1. Display critical patients (heart rate >100).
# 2. Find highest and lowest heart rate.
# 3. Calculate average heart rate.
# 4. Count stable patients (60–100 bpm).
# _ __ __ _ _ _ __ _ __ _  _ _ _ _ '''
# Hospital Patient Monitoring System

heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Display critical patients (heart rate > 100)

print("Critical Patients:")
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient)

# 2. Find highest and lowest heart rate

highest_patient = max(heart_rate, key=heart_rate.get)
lowest_patient = min(heart_rate, key=heart_rate.get)

print("\nHighest Heart Rate:")
print(highest_patient, "(", heart_rate[highest_patient], "bpm )")

print("\nLowest Heart Rate:")
print(lowest_patient, "(", heart_rate[lowest_patient], "bpm )")

# 3. Calculate average heart rate

average_rate = sum(heart_rate.values()) / len(heart_rate)

print("\nAverage Heart Rate:", round(average_rate, 1), "bpm")

# 4. Count stable patients (60–100 bpm)

stable_count = 0

for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable_count += 1

print("Stable Patients:", stable_count)
