fruit = input()
size = input()
count_sets = int(input())
discount = 1

if fruit == "Watermelon":
    if size == "small":
        total_price = count_sets * 2 * 56
    elif size == "big":
        total_price = count_sets * 5 * 28.7
elif fruit == "Mango":
    if size == "small":
        total_price = count_sets * 2 * 36.66
    elif size == "big":
        total_price = count_sets * 5 * 19.6
elif fruit == "Pineapple":
    if size == "small":
        total_price = count_sets * 2 * 42.1
    elif size == "big":
        total_price = count_sets * 5 * 24.8
elif fruit == "Raspberry":
    if size == "small":
        total_price = count_sets * 2 * 20
    elif size == "big":
        total_price = count_sets * 5 * 15.2

if total_price > 1000:
    discount = 0.5
elif 400 <= total_price <= 1000:
    discount = 0.85

total_price = total_price * discount


print(f"{total_price:.2f} lv.")