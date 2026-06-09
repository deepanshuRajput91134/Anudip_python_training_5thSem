import interestcalculator

# input principal
principal = float(input("Enter the principal(in Rs) : "))

if principal < 0:
    exit("Principal amount cannot be negative.")

# input rate
rate = float(input("Enter the rate of interest (in %): "))

if rate < 0:
    exit("Rate of interest cannot be negative.")

# input time
time = int(input("Enter the time period (in years): "))

if time < 0:
    exit("Time period cannot be negative.")

print("---------------------------------------")

# calculate simple interest
si = interestcalculator.simple_interest(principal, rate, time)

# display result
print("Simple Interest : Rs", si)