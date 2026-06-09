 print("----- Rectangle Operations -----")

length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

# Validation
if length <= 0 or breadth <= 0:
    print("Invalid Input! Length and Breadth must be greater than 0.")

else:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of Rectangle =", area)
    print("Perimeter of Rectangle =", perimeter)
