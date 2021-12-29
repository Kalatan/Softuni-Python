budget = float(input())
season = input()
destination = ""
stay = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        stay = "Camp"
    elif season == "winter":
        budget *= 0.7
        stay = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
        stay = "Camp"
    elif season == "winter":
        budget *= 0.8
        stay = "Hotel"
elif budget > 1000:
    destination = "Europe"
    budget *= 0.9
    stay = "Hotel"

print(f"Somewhere in {destination} \n{stay} - {budget:.2f}")
