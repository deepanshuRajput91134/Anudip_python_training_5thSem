side1 = float(input("Enter Side 1: "))
side2 = float(input("Enter Side 2: "))
side3 = float(input("Enter Side 3: "))

if (side1 + side2 > side3) and \
   (side1 + side3 > side2) and \
   (side2 + side3 > side1):

    print("The given sides form a Triangle")

else:
    print("The given sides do NOT form a Triangle")