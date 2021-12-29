season = input()
km_per_month = float(input())

price_per_km = 0
tax = 0.9

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45

total = 4 * km_per_month * price_per_km * tax

print(f"{total:.2f}")
