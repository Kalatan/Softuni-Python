amount = float(input())
unit_from = input()
unit_to = input()

if unit_from == "m":
    if unit_to == "cm":
        amount *= 100
    elif unit_to == "mm":
        amount *= 1000
elif unit_from == "cm":
    if unit_to == "m":
        amount *= 0.01
    elif unit_to == "mm":
        amount *= 10
elif unit_from == "mm":
    if unit_to == "m":
        amount *= 0.001
    elif unit_to == "cm":
        amount *= 0.1

print(f"{amount:.3f}")