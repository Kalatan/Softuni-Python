fruit = input()
day = input()
amount = float(input())

banana_price = 0
apple_price = 0
orange_price = 0
grapefruit_price = 0
kiwi_price = 0
pineapple_price = 0
grapes_price = 0
total = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        total = amount * 2.5
    elif fruit == "apple":
        total = amount * 1.2
    elif fruit == "orange":
        total = amount * 0.85
    elif fruit == "grapefruit":
        total = amount * 1.45
    elif fruit == "kiwi":
        total = amount * 2.7
    elif fruit == "pineapple":
        total = amount * 5.5
    elif fruit == "grapes":
        total = amount * 3.85
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        total = amount * 2.7
    elif fruit == "apple":
        total = amount * 1.25
    elif fruit == "orange":
        total = amount * 0.9
    elif fruit == "grapefruit":
        total = amount * 1.6
    elif fruit == "kiwi":
        total = amount * 3
    elif fruit == "pineapple":
        total = amount * 5.6
    elif fruit == "grapes":
        total = amount * 4.2
    else:
        print("error")
else:
    print("error")

if total == 0:
    pass
else:
    print(f"{total:.2f}")
