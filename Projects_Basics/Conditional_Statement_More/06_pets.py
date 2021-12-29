import math
days = int(input())
food_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

consumed_food = dog_food_per_day * days + cat_food_per_day * days + (turtle_food_per_day / 1000) * days

if consumed_food <= food_kg:
    print(f"{math.floor(food_kg - consumed_food)} kilos of food left.")
else:
    print(f"{math.ceil(consumed_food - food_kg)} more kilos of food are needed.")