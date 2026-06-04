numbers = list(map(int, input("Enter numbers separated by space: ").split()))

max_length = 1
current_length = 1

for i in range(1, len(numbers)):

    if numbers[i] > numbers[i - 1]:
        current_length += 1

    else:
        current_length = 1

    if current_length > max_length:
        max_length = current_length

print("Longest Sequence Length =", max_length)