coins_count_1 = int(input())
coins_count_2 = int(input())
note_count_5 = int(input())
sum = int(input())
check_sum = 0

for a in range(0, coins_count_1 + 1):
    for b in range(0, coins_count_2 + 1):
        for c in range(0, note_count_5 + 1):
            check_sum = a * 1 + b * 2 + c * 5
            if check_sum == sum:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {sum} lv.")