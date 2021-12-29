budget = float(input())
nights_count = int(input())
night_price = float(input())
additional = int(input())

if nights_count > 7:
    night_price *= 0.95

total_price = (nights_count * night_price) + budget * (additional / 100)
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
