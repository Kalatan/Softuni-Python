trip_cost = float(input())
puzzle_count = int(input())
dol_count = int(input())
tedi_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_profit = puzzle_count * 2.6
dol_profit = dol_count * 3
tedi_profit = tedi_count * 4.1
minions_profit = minions_count * 8.2
trucks_profit = trucks_count * 2

total_count = puzzle_count + dol_count + tedi_count + minions_count + trucks_count

total_profit = puzzle_profit + dol_profit + tedi_profit + minions_profit + trucks_profit

if total_count >= 50:
    discount = total_profit * 0.25
    rent = (total_profit - discount) * 0.1
    total = total_profit - discount - rent
    if total >= trip_cost:
        money_left = total - trip_cost
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        needed = trip_cost - total
        print(f"Not enough money! {needed:.2f} lv needed.")
else:
    rent = total_profit * 0.1
    total = total_profit - rent
    if total >= trip_cost:
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        needed = trip_cost - total
        print(f"Not enough money! {needed:.2f} lv needed.")
