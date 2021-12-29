from math import pi
from decimal import Decimal

r = float(input())

area = round(Decimal(r * r * pi), 2)
perimeter = round(Decimal(2 * r * pi), 2)

print(area)
print(perimeter)
