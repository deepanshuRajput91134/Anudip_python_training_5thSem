# Food Delivery Performance Dashboard

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find the fastest delivery time
fastest = min(delivery_times)
print("Fastest Delivery:", fastest, "minutes")

# 2. Find the slowest delivery time
slowest = max(delivery_times)
print("Slowest Delivery:", slowest, "minutes")

# 3. Calculate average delivery time
average = sum(delivery_times) / len(delivery_times)
print("Average Delivery Time:", average, "minutes")

# 4. Display delayed orders (>45 minutes)
delayed_orders = []

for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)

print("\nDelayed Orders:")
print(delayed_orders)

# 5. Categorize deliveries
fast_count = 0
normal_count = 0
delayed_count = 0

for time in delivery_times:

    if time <= 30:
        fast_count += 1

    elif time <= 45:
        normal_count += 1

    else:
        delayed_count += 1

print("\nFast Deliveries:", fast_count)
print("Normal Deliveries:", normal_count)
print("Delayed Deliveries:", delayed_count)