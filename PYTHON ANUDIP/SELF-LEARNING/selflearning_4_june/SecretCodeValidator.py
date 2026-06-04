code = input("Enter 6-digit code: ")

if len(code) == 6 and code.isdigit():

    first_sum = 0
    last_sum = 0

    for i in range(3):
        first_sum += int(code[i])

    for i in range(3, 6):
        last_sum += int(code[i])

    if first_sum == last_sum:
        print("Valid Code")

    else:
        print("Invalid Code")

else:
    print("Invalid Code")