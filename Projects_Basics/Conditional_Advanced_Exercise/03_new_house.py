type_flowers = input()
amount_flowers = int(input())
budget = int(input())
price_per_flower = 0

if type_flowers == "Roses":
    price_per_flower = 5
    if amount_flowers > 80:
            price_per_flower *= 0.9
elif type_flowers == "Dahlias":
    price_per_flower = 3.8
    if amount_flowers > 90:
        price_per_flower *= 0.85
elif type_flowers == "Tulips":
    price_per_flower = 2.8
    if amount_flowers > 80:
        price_per_flower *= 0.85
elif type_flowers == "Narcissus":
    price_per_flower = 3
    if amount_flowers < 120:
        price_per_flower *= 1.15
elif type_flowers == "Gladiolus":
    price_per_flower = 2.5
    if amount_flowers < 80:
        price_per_flower *= 1.2

needed_money = amount_flowers * price_per_flower
difference = abs(budget-needed_money)

if budget >= needed_money:
    print(f"Hey, you have a great garden with {amount_flowers} {type_flowers} and {difference:.2f} leva left.")
elif budget < needed_money:
    print(f"Not enough money, you need {difference:.2f} leva more.")

