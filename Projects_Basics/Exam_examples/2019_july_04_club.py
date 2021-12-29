target = float(input())
cocktail = input()
total_bill = 0
is_enough = False

while cocktail != "Party!":
    cocktails_count = int(input())
    cocktail_price = len(cocktail)
    price = cocktails_count * cocktail_price
    if price % 2 != 0:
        price *= 0.75

    total_bill += price
    if total_bill >= target:
        print(f"Target acquired.")
        print(f"Club income - {total_bill:.2f} leva.")
        is_enough = True
        break

    cocktail = input()

if not is_enough:
    print(f"We need {target - total_bill:.2f} leva more.")
    print(f"Club income - {total_bill:.2f} leva.")

