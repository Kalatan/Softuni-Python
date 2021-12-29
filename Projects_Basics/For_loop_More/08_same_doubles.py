doubles_count = int(input())
value = 0
diff = 0
diff_max = 0
sum_check = 0

for i in range(1, doubles_count * 2 + 1):
    number = int(input())
    value += number
    if i == 2:
        sum_check = value
    if i % 2 == 0 and i > 1:
        if value != sum_check:
            diff = abs(value - sum_check)
            if diff > diff_max:
                diff_max = diff
            sum_check = value
        value = 0

if diff == 0:
    print(f"Yes, value={sum_check}")
else:
    print(f"No, maxdiff={diff_max}")
