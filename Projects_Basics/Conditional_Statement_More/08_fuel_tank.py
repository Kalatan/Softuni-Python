fuel_type = input()
fuel_amount = float(input())

if fuel_type == "Diesel" or fuel_type == "Gas" or fuel_type == "Gasoline":
    if fuel_amount >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif fuel_amount < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
