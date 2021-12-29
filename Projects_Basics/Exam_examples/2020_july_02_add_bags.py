baggage_20_price = float(input())
baggage_weight = float(input())
days_left = int(input())
baggage_count = int(input())

baggge_price = 0

if baggage_weight < 10:
    baggge_price = 0.2 * baggage_20_price
elif 10 <= baggage_weight <= 20:
    baggge_price = 0.5 * baggage_20_price
elif baggage_weight > 20:
    baggge_price = baggage_20_price

if days_left > 30:
    baggge_price *= 1.1
elif 7 <= days_left <= 30:
    baggge_price *= 1.15
elif days_left < 7:
    baggge_price *= 1.4

total = baggge_price * baggage_count

print(f"The total price of bags is: {total:.2f} lv.")
