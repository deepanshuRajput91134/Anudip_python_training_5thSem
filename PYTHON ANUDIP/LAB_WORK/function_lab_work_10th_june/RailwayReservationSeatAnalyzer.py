# #Railway Reservation Seat Analyzer
# '''_ _ _ _ _ _ _ __ _ _ _ __ _ _ _ _ _ _ _ _ _
# Create the following functions:
# 1. count_seats(seats)
# Returns the number of booked and available seats.
# 2. first_available(seats)
# Returns the seat number of the first available seat.
# 3. occupancy_percentage(seats)
# Returns the percentage of occupied seats.
# 4. display_available_seats(seats)
# Displays all available seat numbers.
#  _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'''
 # List containing seat status
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function to count booked and available seats 
def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1
        else:
            available += 1

    return booked, available
    # Function to find first available seat number
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1      # Seat numbers start from 1

# Function to calculate occupancy percentage
def occupancy_percentage(seats):
    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1

    return (booked / len(seats)) * 100

# Function to display all available seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")

# Function Calls
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("Occupancy Percentage:",
      round(occupancy_percentage(seats), 2), "%")

display_available_seats(seats)