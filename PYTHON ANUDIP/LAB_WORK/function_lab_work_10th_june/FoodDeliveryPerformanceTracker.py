#Food Delivery Performance Tracker
'''_ _ _ _ _ _. _ _ _ __ _ _ _ _ _ ___ _ _
Create the following functions:
1. fastest_delivery(times)
Returns the shortest delivery time.
2. delayed_orders(times)
Returns a list of orders taking more than 45 minutes.
3. average_delivery_time(times)
Returns the average delivery time.
4. delivery_category(times)
Displays order categories:
• Fast → ≤ 30 minutes
• Normal → 31–45 minutes
• Delayed → > 45 minutes
 __. _ _ _ _ __ _ __ _ _ _'''
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Fastest delivery
def fastest_delivery(times):
    return min(times)

# 2. Delayed orders (>45 min)
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    return delayed

# 3. Average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# 4. Delivery category
def delivery_category(times):
    for t in times:
        if t <= 30:
            print(t, "-> Fast")
        elif t <= 45:
            print(t, "-> Normal")
        else:
            print(t, "-> Delayed")


# Function calls
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders:", delayed_orders(delivery_time))
print("Average Delivery Time:", round(average_delivery_time(delivery_time), 1), "minutes")

print("\nCategories:")
delivery_category(delivery_time)