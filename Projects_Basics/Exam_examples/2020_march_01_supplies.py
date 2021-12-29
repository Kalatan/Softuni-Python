pen_packs = int(input())
marker_packs = int(input())
cleaner = float(input())
discount = int(input())

price_pens = pen_packs * 5.8
price_markers = marker_packs * 7.2
price_cleaner = cleaner * 1.2

total = (price_pens + price_markers + price_cleaner) - ((price_pens + price_markers + price_cleaner) * discount / 100)

print(f"{total:.3f}")