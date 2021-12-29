from decimal import Decimal

cel = float(input())
far = Decimal((cel * 9/5) + 32)

print(round(far, 2))
