number = int(input())

for num in range(1111, 9999 + 1):
    is_special = True
    string_of_num = str(num)
    for index in string_of_num:
        if int(index) > 0 and number % int(index) == 0:
            pass
        else:
            is_special = False
    if is_special:
        print(num, end=" ")
