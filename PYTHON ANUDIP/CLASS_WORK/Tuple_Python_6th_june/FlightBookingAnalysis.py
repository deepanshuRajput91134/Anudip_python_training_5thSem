''' _ _ _ _. __
Write a Python program to:
1. Display all passengers whose booking status is Confirmed.
2. Count the number of passengers travelling to Delhi.
3. Count Confirmed, Waiting, and Cancelled bookings separately.
4. Create a list containing passenger IDs with Waiting status.
5. Determine which destination has the highest number of bookings.
_ _ _ _ _ _ _'''
# Flight Booking Analysis

# Tuple containing passenger booking records
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display all passengers whose booking status is Confirmed
print("Confirmed Passengers:")

for passenger in bookings:
    if passenger[2] == "Confirmed":
        print(passenger[0], passenger[1])

# 2. Count number of passengers travelling to Delhi
delhi_count = 0

for passenger in bookings:
    if passenger[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count Confirmed, Waiting, and Cancelled bookings
confirmed = 0
waiting = 0
cancelled = 0

for passenger in bookings:
    if passenger[2] == "Confirmed":
        confirmed += 1
    elif passenger[2] == "Waiting":
        waiting += 1
    elif passenger[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# 4. Create a list containing passenger IDs with Waiting status
waiting_list = []

for passenger in bookings:
    if passenger[2] == "Waiting":
        waiting_list.append(passenger[0])

print("\nWaiting List:")
print(waiting_list)

# 5. Determine destination with highest number of bookings

destination_count = {}

for passenger in bookings:
    destination = passenger[1]

    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

most_booked = max(destination_count, key=destination_count.get)

print("\nMost Booked Destination:")
print(most_booked)