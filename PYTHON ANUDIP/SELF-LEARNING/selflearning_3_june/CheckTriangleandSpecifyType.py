print("----- Triangle Checker -----")

side1 = float(input("Enter Side 1: "))
side2 = float(input("Enter Side 2: "))
side3 = float(input("Enter Side 3: "))

# Check Triangle Validity
if (side1 + side2 > side3) and \
   (side1 + side3 > side2) and \
   (side2 + side3 > side1):

    print("The given sides form a Triangle")

    # Type of Triangle
    if side1 == side2 == side3:
        print("Type: Equilateral Triangle")

    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Type: Isosceles Triangle")

    else:
        print("Type: Scalene Triangle")

else:
    print("The given sides do NOT form a Triangle")