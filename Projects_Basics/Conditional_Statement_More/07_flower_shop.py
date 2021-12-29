import math

magnolii = int(input())
zumbuli = int(input())
rozi = int(input())
kaktusi = int(input())
present_price = float(input())

total = 0.95 * (magnolii * 3.25 + zumbuli * 4 + rozi * 3.5 + kaktusi * 8)

if total >= present_price:
    print(f"She is left with {math.floor(total - present_price)} leva.")
else:
    print(f'She will have to borrow {math.ceil(present_price - total)} leva.')