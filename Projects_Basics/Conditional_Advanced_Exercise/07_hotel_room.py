month = input()
nights = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    apartment = 65
    if nights <= 7:
        studio = 50
    elif nights <= 14:
        studio = 50 * 0.95
    elif nights > 14:
        studio = 50 * 0.7
        apartment = 65 * 0.9
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio = 75.2 * 0.8
        apartment = 68.7 * 0.9
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment = 77 * 0.9

total_studio = nights * studio
total_apartment = nights * apartment

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")