import math

lily_years = int(input())
washmachine_price = float(input())
toy_price = int(input())
toy_count = 0
money_count = 0

for n in range(1, lily_years + 1):
    if n % 2 == 1:
        toy_count += 1
    elif n % 2 == 0:
        money_count += (n / 2) * 10

money_collected = money_count - math.floor(lily_years / 2)
toy_money = toy_count * toy_price
total = money_collected + toy_money
difference = abs(total - washmachine_price)

if total >= washmachine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
