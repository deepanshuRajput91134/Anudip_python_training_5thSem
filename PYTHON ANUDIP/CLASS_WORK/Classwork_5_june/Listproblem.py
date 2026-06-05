# WAP to create a list of 20 numbers given by user
# and remove all duplicates of another number entered by user

numbers = []

# Input 20 numbers
print("Enter 20 numbers:")
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal List:")
print(numbers)

# Ask user for number to remove
remove_num = int(input("\nEnter a number to remove from list: "))

# Remove all duplicates of that number
while remove_num in numbers:
    numbers.remove(remove_num)

print("\nUpdated List:")
print(numbers)