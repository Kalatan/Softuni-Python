season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

price_per_night = 0
sport = ""

if group_type == "boys":
    if season == "Winter":
        price_per_night = 9.6
        sport = "Judo"
    elif season == "Spring":
        price_per_night = 7.2
        sport = "Tennis"
    elif season == "Summer":
        price_per_night = 15
        sport = "Football"
elif group_type == "girls":
    if season == "Winter":
        price_per_night = 9.6
        sport = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.2
        sport = "Athletics"
    elif season == "Summer":
        price_per_night = 15
        sport = "Volleyball"
elif group_type == "mixed":
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.5
        sport = "Cycling"
    elif season == "Summer":
        price_per_night = 20
        sport = "Swimming"

if students_count >= 50:
    price_per_night *= 0.5
elif 20 <= students_count < 50:
    price_per_night *= 0.85
elif 10 <= students_count < 20:
    price_per_night *= 0.95
else:
    price_per_night = price_per_night

total = price_per_night * nights_count * students_count
print(f"{sport} {total:.2f} lv.")

