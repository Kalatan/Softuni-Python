bottles = int(input())
dish_input_text = input()

bottles_volume = bottles * 750
input_count = 0
plate_count = 0
plate_volume = 0
pot_count = 0
pot_volume = 0
not_enough = False

while dish_input_text != "End":
    dish_int = int(dish_input_text)
    input_count += 1
    if input_count % 3 == 0:
        pot_count += dish_int
        pot_volume = 0
        pot_volume += pot_count * 15
    else:
        plate_count += dish_int
        plate_volume = 0
        plate_volume = plate_count * 5

    dish_total_volume = 0
    dish_total_volume = pot_volume + plate_volume

    if dish_total_volume <= bottles_volume:
        dish_input_text = input()
    else:
        print(f"Not enough detergent, {dish_total_volume - bottles_volume} ml. more necessary!")
        not_enough = True
        break

if not_enough:
    pass
else:
    print(f"Detergent was enough!")
    print(f"{plate_count} dishes and {pot_count} pots were washed.")
    print(f"Leftover detergent {bottles_volume - dish_total_volume} ml.")