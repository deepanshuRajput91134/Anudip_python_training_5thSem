high_transactions = 0
low_transactions = 0
total_amount = 0

while True:

    amount = int(input("Enter transaction amount (-1 to stop): "))

    if amount == -1:
        break

    total_amount += amount

    if amount > 50000:
        high_transactions += 1

    if amount < 1000:
        low_transactions += 1

print("Transactions above ₹50,000:", high_transactions)
print("Transactions below ₹1,000:", low_transactions)
print("Total Transaction Amount:", total_amount)