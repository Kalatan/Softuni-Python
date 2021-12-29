from decimal import Decimal

skumria_price = float(input())
caca_price = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_price = 0.6 * skumria_price + skumria_price
safrid_price = 0.8 * caca_price + caca_price
midi_price = 7.5

total_price = Decimal(palamud * palamud_price + safrid * safrid_price + midi * midi_price)

print(round(total_price, 2))

