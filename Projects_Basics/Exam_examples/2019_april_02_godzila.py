budget = float(input())
statists = int(input())
garment_price = float(input())
decor = budget * 0.1

if statists > 150:
    garment_price *= 0.9

total = statists * garment_price + decor
diff = abs(budget - total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")