num = input("Enter a number: ")

length = len(num)

if length % 2 == 0:

    mid = length // 2

    left = num[:mid]
    right = num[mid:]

    if left == right:
        print("Mirror Number")

    else:
        print("Not a Mirror Number")

else:
    print("Not a Mirror Number")