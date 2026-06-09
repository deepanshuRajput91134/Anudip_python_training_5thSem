# Program for The operations of two-dimensional figures
"""
Problem Statement:
Create a program which provides a menu to the user to select a two-dimensional figure (rectangle, square, circle).
After selecting the figure user is again asked to provide the input of corresponding data for for the figure .
After input og corresponding data again provide a menu to the user to select the operation (area, perimeter) to be performed on the figure.
and as per the user selection perform the operation and display the result to the user.
This task is repeated again and again until the user selects the option to exit from that figure and back to previous menu to select another figure or exit from the program.
"""
# import the mensuration module
import mensuration
# create a menu for the user to select a two-dimensional figure
while True:
    print("Select a two-dimensional figure: ")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # ----------------------------get the length and width of the rectangle from the user----------------------------------
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        while True:
            print("Select an operation: ")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit")
            operation = int(input("Enter your choice: "))
            if operation == 1:
                area = mensuration.rectangle_area(length, width)
                print("The area of the rectangle is: ", area)
            elif operation == 2:
                perimeter = mensuration.rectangle_perimeter(length, width)
                print("The perimeter of the rectangle is: ", perimeter)
            elif operation == 3:
                break
            else:
                print("Invalid choice! Please try again.")
    elif choice == 2:
        #------------------------- get the side of the square from the user--------------------------------------
        side = float(input("Enter the side of the square: "))
        while True:
            print("Select an operation: ")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit")
            operation = int(input("Enter your choice: "))
            if operation == 1:
                area = mensuration.square_area(side)
                print("The area of the square is: ", area)
            elif operation == 2:
                perimeter = mensuration.square_perimeter(side)
                print("The perimeter of the square is: ", perimeter)
            elif operation == 3:
                break
            else:
                print("Invalid choice! Please try again.")
    elif choice == 3:
        # ----------------------------------get the radius of the circle from the user-------------------------------------
        radius = float(input("Enter the radius of the circle: "))
        while True:
            print("Select an operation: ")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit")
            operation = int(input("Enter your choice: "))
            if operation == 1:
                area = mensuration.circle_area(radius)
                print("The area of the circle is: ", area)
            elif operation == 2:
                perimeter = mensuration.circle_perimeter(radius)
                print("The perimeter of the circle is: ", perimeter)
            elif operation == 3:
                break
            else:
                print("Invalid choice! Please try again.")
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")