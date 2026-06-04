num = input("Enter a number: ")

peak_found = False
flag = True

for i in range(len(num) - 1):

    if num[i] < num[i + 1] and not peak_found:
        continue

    elif num[i] > num[i + 1]:
        peak_found = True

    else:
        flag = False
        break

if peak_found and flag:
    print("Mountain Number")

else:
    print("Not a Mountain Number")