start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
count_combination = 0
is_break = False

for first_num in range(start_interval, end_interval + 1):
    for second_num in range(start_interval, end_interval + 1):
        count_combination += 1
        if first_num + second_num == magic_number:
            print(f"Combination N:{count_combination} ({first_num} + {second_num} = {magic_number})")
            is_break = True
            break
    if is_break:
        break

if is_break:
    pass
else:
    print(f"{count_combination} combinations - neither equals {magic_number}")