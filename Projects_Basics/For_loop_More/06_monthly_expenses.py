months = int(input())
water = 0
internet = 0
electricity = 0

for month in range(1, months + 1):
    month_electricity = float(input())
    water += 20
    internet += 15
    electricity += month_electricity
    other = (water + internet + electricity) * 1.2

average = (water + internet + electricity + other) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")