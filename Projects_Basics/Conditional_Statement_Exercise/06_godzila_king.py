budget = float(input())
statists = int(input())
garment_price_stat = float(input())

decor = budget * 0.1

if statists > 150:
    garment_price_stat *= 0.9

total = statists * garment_price_stat + decor

if total <= budget:
    left_money = budget - total
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
elif total > budget:
    needed_money = total - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")


