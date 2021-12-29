trip_days = int(input())
room_type = input()
assessment = input()
trip_nights = trip_days - 1
night_price = 0

if room_type == "room for one person":
    night_price = 18
elif room_type == "apartment":
    if trip_nights < 10:
        night_price = 25 * 0.7
    elif trip_nights <= 15:
        night_price = 25 * 0.65
    elif trip_nights > 15:
        night_price = 25 * 0.5
elif room_type == "president apartment":
    if trip_nights < 10:
        night_price = 35 * 0.9
    elif trip_nights <= 15:
        night_price = 35 * 0.85
    elif trip_nights > 15:
        night_price = 35 * 0.8

total = trip_nights * night_price

if assessment == "positive":
    total *= 1.25
elif assessment == "negative":
    total *= 0.9

print(f"{total:.2f}")