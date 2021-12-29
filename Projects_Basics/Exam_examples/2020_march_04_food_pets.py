days_count = int(input())
food = float(input())
dog_food_sum = 0
cat_food_sum = 0
counter_days = 0
bonus_biscuits = 0

for day in range(1, days_count + 1):
    dog_food = int(input())
    cat_food = int(input())

    counter_days += 1
    dog_food_sum += dog_food
    cat_food_sum += cat_food
    if counter_days % 3 == 0:
        bonus_biscuits += dog_food + cat_food

biscuits = round(0.1 * bonus_biscuits)

total_eaten_food = dog_food_sum + cat_food_sum

eaten_perc = (total_eaten_food / food) * 100
dog_perc = (dog_food_sum / total_eaten_food) * 100
cat_perc = (cat_food_sum / total_eaten_food) * 100

print(f"Total eaten biscuits: {biscuits}gr.")
print(f"{eaten_perc:.2f}% of the food has been eaten.")
print(f"{dog_perc:.2f}% eaten from the dog.")
print(f"{cat_perc:.2f}% eaten from the cat.")

