days_stay = int(input())
room_type = input()
assess = input()

nights_stay = days_stay - 1
price_per_night = 0

if nights_stay < 10:
    if room_type == "room for one person":
        price_per_night = 18
    elif room_type == "apartment":
        price_per_night = 25 * 0.7
    elif room_type == "president apartment":
        price_per_night = 35 * 0.9
elif 10 <= nights_stay <= 15:
    if room_type == "room for one person":
        price_per_night = 18
    elif room_type == "apartment":
        price_per_night = 25 * 0.65
    elif room_type == "president apartment":
        price_per_night = 35 * 0.85
elif 15 < nights_stay:
    if room_type == "room for one person":
        price_per_night = 18
    elif room_type == "apartment":
        price_per_night = 25 * 0.5
    elif room_type == "president apartment":
        price_per_night = 35 * 0.8

total_price = nights_stay * price_per_night

if assess == "positive":
    total_price = total_price * 1.25
elif assess == "negative":
    total_price = total_price * 0.9

print(f"{total_price:.2f}")
