hrizantemi = int(input())
rozi = int(input())
laleta = int(input())
season = input()
holiday = input()

flowers_count = hrizantemi + rozi + laleta
total = 0
hrizantemi_price = 0
rozi_price = 0
laleta_price = 0

if season == "Spring" or season == "Summer":
    hrizantemi_price = 2
    rozi_price = 4.1
    laleta_price = 2.5
    total = hrizantemi * hrizantemi_price + rozi * rozi_price + laleta * laleta_price
elif season == "Autumn" or season == "Winter":
    hrizantemi_price = 3.75
    rozi_price = 4.5
    laleta_price = 4.15
    total = hrizantemi * hrizantemi_price + rozi * rozi_price + laleta * laleta_price

if holiday == "Y":
    total *= 1.15

if season == "Spring" and laleta > 7:
    total *= 0.95
elif season == "Winter" and rozi >= 10:
    total *= 0.9
if flowers_count > 20:
    total *= 0.8

cash = total + 2
print(f"{cash:.2f}")
