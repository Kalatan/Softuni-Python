hour = int(input())
minutes = int(input())

hour_min = hour * 60
total_min = hour_min + minutes + 15

total_hour = total_min // 60
print_min = total_min % 60

if total_hour >= 24:
    total_hour -= 24

if print_min < 10:
    print(f"{total_hour}:0{print_min}")
else:
    print(f"{total_hour}:{print_min}")