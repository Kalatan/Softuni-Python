input_number = int(input())

for num in range(1111, 9999 + 1):
    string_of_num = str(num)
    str_first_num = string_of_num[0]
    str_second_num = string_of_num[1]
    str_third_num = string_of_num[2]
    str_forth_num = string_of_num[3]

    first_num = int(str_first_num)
    second_num = int(str_second_num)
    third_num = int(str_third_num)
    forth_num = int(str_forth_num)
    if first_num != 0 and second_num != 0 and third_num != 0 and forth_num != 0:
        if (first_num + second_num) == (third_num + forth_num):
            if input_number % (first_num + second_num) == 0:
                print(num, end=" ")
    else:
        pass