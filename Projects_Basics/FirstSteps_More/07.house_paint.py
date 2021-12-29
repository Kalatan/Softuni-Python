from decimal import Decimal
x = float(input())
y = float(input())
h = float(input())

green_norm = 3.4
red_norm = 4.3

openings = 2 * 1.2 + 2 * (1.5 * 1.5)
walls = (x * 2 + y * 2) * x - openings
roof = (x * y * 2) + 2 * (x * h / 2)

green_paint = Decimal(walls / green_norm)
red_paint = Decimal(roof / red_norm)

print(round(green_paint, 2))
print(round(red_paint, 2))
