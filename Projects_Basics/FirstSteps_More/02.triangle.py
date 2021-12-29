from decimal import Decimal

a = float(input())
h = float(input())

area = Decimal(a * h / 2)
print(round(area, 2))

