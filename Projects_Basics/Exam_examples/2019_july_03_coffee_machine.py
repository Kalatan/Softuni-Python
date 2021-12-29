drink = input()
sugar = input()
drinks_count = int(input())
bill = 0

if drink == "Espresso":
    if sugar == "Without":
        bill = 0.65 * drinks_count * 0.9
    elif sugar == "Normal":
        bill = drinks_count
    elif sugar == "Extra":
        bill = drinks_count * 1.2

    if drinks_count >= 5:
        bill *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        bill = 0.65 * drinks_count
    elif sugar == "Normal":
        bill = drinks_count * 1.2
    elif sugar == "Extra":
        bill = drinks_count * 1.6
elif drink == "Tea":
    if sugar == "Without":
        bill = 0.65 * drinks_count * 0.5
    elif sugar == "Normal":
        bill = drinks_count * 0.6
    elif sugar == "Extra":
        bill = drinks_count * 0.7

if bill > 15:
    bill *= 0.8

print(f"You bought {drinks_count} cups of {drink} for {bill:.2f} lv.")
