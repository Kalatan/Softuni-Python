film_name = input()
hall_type = input()
tickets = int(input())
total = 0

if hall_type == "normal":
    if film_name == "A Star Is Born":
        total = tickets * 7.5
    elif film_name == "Bohemian Rhapsody":
        total = tickets * 7.35
    elif film_name == "Green Book":
        total = tickets * 8.15
    elif film_name == "The Favourite":
        total = tickets * 8.75
elif hall_type == "luxury":
    if film_name == "A Star Is Born":
        total = tickets * 10.5
    elif film_name == "Bohemian Rhapsody":
        total = tickets * 9.45
    elif film_name == "Green Book":
        total = tickets * 10.25
    elif film_name == "The Favourite":
        total = tickets * 11.55
elif hall_type == "ultra luxury":
    if film_name == "A Star Is Born":
        total = tickets * 13.5
    elif film_name == "Bohemian Rhapsody":
        total = tickets * 12.75
    elif film_name == "Green Book":
        total = tickets * 13.25
    elif film_name == "The Favourite":
        total = tickets * 13.95

print(f"{film_name} -> {total:.2f} lv.")