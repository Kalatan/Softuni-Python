import math

days_count = int(input())
food_storage = int(input())
food_per_day_1 = float(input())
food_per_day_2 = float(input())
food_per_day_3 = float(input())

needed_food = days_count * (food_per_day_1 + food_per_day_2 + food_per_day_3)

diff = abs(food_storage - needed_food)

if food_storage >= needed_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")