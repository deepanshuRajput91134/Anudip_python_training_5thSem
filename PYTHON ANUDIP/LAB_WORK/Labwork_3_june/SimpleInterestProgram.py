print("----- Simple Interest Calculator -----")

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Validation
if principal <= 0 or rate <= 0 or time <= 0:
    print("Invalid Input! Values must be greater than 0.")

else:
    simple_interest = (principal * rate * time) / 100

    print("Simple Interest =", simple_interest)