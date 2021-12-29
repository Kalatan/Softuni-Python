from decimal import Decimal

b1 = float(input())
b2 = float(input())
h = float(input())

area = Decimal((b1 + b2) * h / 2)
print(round(area, 2))

