# WAP to create a list of 20 numbers given by user
# and remove all duplicates of another number entered by user

numbers = []

print("Enter any 20 numbers:")

for i in range(20):
    num = int(input())
    
    # Append into list
    numbers.append(num)

print("----------------------------")

element = int(input("Enter any number to remove its duplicate: "))

# Finding the frequency of given number
frequency = numbers.count(element)

if frequency == 0:
    print("Element not found")

elif frequency == 1:
    print("No duplicates found")

else:
    # Reversing the list
    numbers.reverse()

    for i in range(1, frequency):
        numbers.remove(element)

    # Reversing the list again
    numbers.reverse()

    print("After removing duplicates")
    print(numbers)