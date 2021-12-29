will_sleep = input()
climbed_meters = 5364
days = 1
is_failed = False

while will_sleep != "END":
    meters = int(input())
    if will_sleep == "Yes":
        days += 1

    if days <= 5:
        climbed_meters += meters
    else:
        is_failed = True
        break

    if climbed_meters >= 8848:
        print(f"Goal reached for {days} days!")
        break
    else:
        will_sleep = input()

if will_sleep == "END" or is_failed:
    print("Failed!")
    print(climbed_meters)
else:
    pass

