ppl_count = int(input())
nights_count = int(input())
transport_cards_count = int(input())
museum_cards_count = int(input())

total_price = ppl_count * (nights_count * 20 + transport_cards_count * 1.6 + museum_cards_count * 6)

total = total_price * 1.25

print(f"{total:.2f}")