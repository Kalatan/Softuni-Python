hall_rent = int(input())

cake = float(0.2*hall_rent)
drinks = float(cake - (0.45*cake))
animator = float(hall_rent/3)
total = hall_rent + cake + drinks + animator

print(total)