walk_min = int(input())
count_daily_walks = int(input())
daily_calories = int(input())

burn_calories = (walk_min * count_daily_walks) * 5

if burn_calories < daily_calories / 2:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")
else:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")