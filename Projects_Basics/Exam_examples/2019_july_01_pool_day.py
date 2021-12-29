import math

ppl_count = int(input())
entry_price = float(input())
lounge_price = float(input())
umbrella_price = float(input())

total_price = ppl_count * entry_price + math.ceil(ppl_count * 0.75) * lounge_price + math.ceil(ppl_count * 0.5) * umbrella_price

print(f"{total_price:.2f} lv.")
