import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())
wine = x * y * 0.4 / 2.5

if wine >= z:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(wine - z)} liters left -> {math.ceil((wine - z) / workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(z - wine)} liters wine needed.")

