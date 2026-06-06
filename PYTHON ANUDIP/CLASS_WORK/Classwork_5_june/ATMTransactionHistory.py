# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Variables
balance = 0
deposits = []
withdrawals = []

# Assume initial values
largest_deposit = transactions[0]
largest_withdrawal = transactions[1]

# Loop through transactions
for amount in transactions:


     # Calculate balance
    balance += amount

    # Check deposits
    if amount > 0:

        deposits.append(amount)

        # Find largest deposit
        if amount > largest_deposit:
            largest_deposit = amount

    # Check withdrawals
    else:

        withdrawals.append(amount)

        # Find largest withdrawal
        if amount < largest_withdrawal:
            largest_withdrawal = amount

# Display output
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal) 