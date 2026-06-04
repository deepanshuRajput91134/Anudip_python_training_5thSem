balance = 10000

while True:

    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient Balance")

        else:
            balance -= amount
            print("Withdrawal Successful")

    elif choice == 4:
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice")