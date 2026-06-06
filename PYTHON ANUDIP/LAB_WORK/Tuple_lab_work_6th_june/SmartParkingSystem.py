 #Smart Parking System
'''_ _ _ _ _ _ _ _ _ _ _ _
• Count occupied and available slots.
• Find the first available slot.
• Display all available slot numbers.
• Check whether parking occupancy exceeds 75%.
_ _ _ _ _ _ _ _ _ _ __ _ __'''
# Smart Parking System

slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = slots.count(1)
available = slots.count(0)

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# First available slot
first_available = slots.index(0) + 1

print("\nFirst Available Slot:", first_available)

# All available slots
print("\nAvailable Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# Parking occupancy check
occupancy = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy)

if occupancy > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")