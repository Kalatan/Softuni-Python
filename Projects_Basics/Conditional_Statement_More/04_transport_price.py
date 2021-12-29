km = int(input())
travel_period = input()

taxi_day = km * 0.79 + 0.7
taxi_night = km * 0.90 + 0.7
bus = km * 0.09
train = km * 0.06
travel_mode = taxi_day

if km < 20:
    if travel_period == "day":
        print(f"{taxi_day:.2f}")
    elif travel_period == "night":
        print(f"{taxi_night:.2f}")
elif km < 100:
    print(f"{bus:.2f}")
else:
    print(f"{train:.2f}")
