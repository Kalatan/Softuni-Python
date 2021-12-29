import math
year_type = input()
vacation_days = int(input())
home_town_weekends = int(input())

normal_plays = ((48 - home_town_weekends) * 3 / 4) + (vacation_days * 2 / 3) + home_town_weekends
leap_plays = normal_plays * 1.15

if year_type == "normal":
    print(math.floor(normal_plays))
elif year_type == "leap":
    print(math.floor(leap_plays))