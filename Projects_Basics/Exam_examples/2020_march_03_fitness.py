our_sum = float(input())
sex = input()
age = int(input())
sport = input()
price = 0

if sport == "Gym" and sex == "m":
    if age <= 19:
        price = 42 * 0.8
    else:
        price = 42
elif sport == "Gym" and sex == "f":
    if age <= 19:
        price = 35 * 0.8
    else:
        price = 35
elif sport == "Boxing" and sex == "m":
    if age <= 19:
        price = 41 * 0.8
    else:
        price = 41
elif sport == "Boxing" and sex == "f":
    if age <= 19:
        price = 37 * 0.8
    else:
        price = 37
elif sport == "Yoga" and sex == "m":
    if age <= 19:
        price = 45 * 0.8
    else:
        price = 45
elif sport == "Yoga" and sex == "f":
    if age <= 19:
        price = 42 * 0.8
    else:
        price = 42
elif sport == "Zumba" and sex == "m":
    if age <= 19:
        price = 34 * 0.8
    else:
        price = 34
elif sport == "Zumba" and sex == "f":
    if age <= 19:
        price = 31 * 0.8
    else:
        price = 31
elif sport == "Dances" and sex == "m":
    if age <= 19:
        price = 51 * 0.8
    else:
        price = 51
elif sport == "Dances" and sex == "f":
    if age <= 19:
        price = 53 * 0.8
    else:
        price = 53
elif sport == "Pilates" and sex == "m":
    if age <= 19:
        price = 39 * 0.8
    else:
        price = 39
elif sport == "Pilates" and sex == "f":
    if age <= 19:
        price = 37 * 0.8
    else:
        price = 37

if price <= our_sum:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${(price - our_sum):.2f} more.")