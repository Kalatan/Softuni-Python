fuel_type = input()
fuel_amount = float(input())
card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_price_disc = gasoline_price - 0.18
diesel_price_disc = diesel_price - 0.12
gas_price_disc = gas_price - 0.08

if fuel_type == "Diesel" and card == "Yes":
    fuel = diesel_price_disc * fuel_amount
elif fuel_type == "Diesel" and card == "No":
    fuel = diesel_price * fuel_amount
elif fuel_type == "Gas" and card == "Yes":
    fuel = gas_price_disc * fuel_amount
elif fuel_type == "Gas" and card == "No":
    fuel = gas_price * fuel_amount
elif fuel_type == "Gasoline" and card == "Yes":
    fuel = gasoline_price_disc * fuel_amount
elif fuel_type == "Gasoline" and card == "No":
    fuel = gasoline_price * fuel_amount

if fuel_amount < 20:
    print(f"{(fuel):.2f} lv.")
elif fuel_amount <= 25:
    print(f"{(fuel * 0.92):.2f} lv.")
elif fuel_amount > 25:
    print(f"{(fuel * 0.9):.2f} lv.")