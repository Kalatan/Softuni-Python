budget = float(input())
ticket_type = input()
fans_count = int(input())

tickets_price = 0
transport = 0

if ticket_type == "VIP":
    tickets_price = fans_count * 499.99
elif ticket_type == "Normal":
    tickets_price = fans_count * 249.99

if 1 <= fans_count <= 4:
    transport = budget * 0.75
elif 5 <= fans_count <= 9:
    transport = budget * 0.6
elif 10 <= fans_count <= 24:
    transport = budget * 0.5
elif 25 <= fans_count <= 49:
    transport = budget * 0.4
elif 50 <= fans_count:
    transport = budget * 0.25

total = transport + tickets_price
difference = abs(budget - total)

if budget >= total:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < total:
    print(f"Not enough money! You need {difference:.2f} leva.")