steps = int(input())
points = 0
first_interval = 0
second_interval = 0
third_interval = 0
fourth_interval = 0
fifth_interval = 0
invalid_interval = 0

for n in range(1, steps + 1):
    number = int(input())
    # points += number
    if 0 <= number <= 9:
        first_interval += 1
        points += number * 0.2
    elif 10 <= number <= 19:
        second_interval += 1
        points += number * 0.3
    elif 20 <= number <= 29:
        third_interval += 1
        points += number * 0.4
    elif 30 <= number <= 39:
        fourth_interval += 1
        points += 50
    elif 40 <= number <= 50:
        fifth_interval += 1
        points += 100
    else:
        invalid_interval += 1
        points /= 2

first_interval_perc = first_interval / steps * 100
second_interval_perc = second_interval / steps * 100
third_interval_perc = third_interval / steps * 100
fourth_interval_perc = fourth_interval / steps * 100
fifth_interval_perc = fifth_interval / steps * 100
invalid_interval_perc = invalid_interval / steps * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {first_interval_perc:.2f}%")
print(f"From 10 to 19: {second_interval_perc:.2f}%")
print(f"From 20 to 29: {third_interval_perc:.2f}%")
print(f"From 30 to 39: {fourth_interval_perc:.2f}%")
print(f"From 40 to 50: {fifth_interval_perc:.2f}%")
print(f"Invalid numbers: {invalid_interval_perc:.2f}%")
