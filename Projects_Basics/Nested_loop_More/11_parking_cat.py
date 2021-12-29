days_count = int(input())
hours_per_day = int(input())
total = 0
price_per_hour = 0

for day in range(1, days_count + 1):
    hourly_sum = 0
    for hour in range(1, hours_per_day + 1):
        if (day % 2 == 0 and hour % 2 == 0) or (day % 2 != 0 and hour % 2 != 0):
            price_per_hour = 1
        elif day % 2 == 0 and hour % 2 != 0:
            price_per_hour = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price_per_hour = 1.25

        hourly_sum += price_per_hour

    total += hourly_sum
    print(f"Day: {day} - {hourly_sum:.2f} leva")
print(f"Total: {total:.2f} leva")