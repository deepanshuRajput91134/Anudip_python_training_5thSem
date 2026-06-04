print("----- Triangle Operations -----")

side1 = float(input("Enter Side 1: "))
side2 = float(input("Enter Side 2: "))
side3 = float(input("Enter Side 3: "))

# Perimeter
perimeter = side1 + side2 + side3

# Semi-perimeter
s = perimeter / 2

# Area using Heron's Formula
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("\nPerimeter of Triangle =", perimeter)
print("Area of Triangle =", area)

# Type of Triangle
if side1 == side2 == side3:
    print("Triangle Type: Equilateral Triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Triangle Type: Isosceles Triangle")

else:
    print("Triangle Type: Scalene Triangle")