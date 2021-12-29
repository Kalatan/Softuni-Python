food_kg = int(input())
command = input()
food_sum = 0

while command != "Adopted":
    food_meal = int(command)
    food_sum += food_meal
    command = input()

diff = abs((food_kg * 1000) - food_sum)
if food_sum <= (food_kg * 1000):
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")

