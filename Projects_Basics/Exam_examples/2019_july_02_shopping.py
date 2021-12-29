budget = float(input())
graphic_cards = int(input())
processors = int(input())
memory_cards = int(input())

graphic_price = graphic_cards * 250
processor_price = 0.35 * graphic_price * processors
memoty_price = 0.1 * graphic_price * memory_cards
total_price = graphic_price + processor_price + memoty_price

if graphic_cards > processors:
    total_price *= 0.85

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")