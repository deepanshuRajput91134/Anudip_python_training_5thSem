# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Empty list for consecutive pairs
consecutive_pairs = []

# Loop through list
for i in range(len(numbers) - 1):

    # Check consecutive numbers
    if numbers[i] + 1 == numbers[i + 1]:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store pair in list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Print all consecutive pairs
print(consecutive_pairs)