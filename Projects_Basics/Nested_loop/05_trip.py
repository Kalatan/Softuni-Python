destination = input()

while destination != "End":
    price_trip = float(input())
    available_money = 0
    while available_money < price_trip:
        saved_money = float(input())
        available_money += saved_money
    else:
        print(f"Going to {destination}!")
    destination = input()
