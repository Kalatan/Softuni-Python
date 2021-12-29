start_first_in = int(input())
start_second_in = int(input())

start_first_out = int(input())
start_second_out = int(input())
counter = 0
is_enough = False

for first_in in range(start_first_in, 8 + 1):
    for second_in in range(9, start_second_in - 1, -1):

        for first_out in range(start_first_out, 8 + 1):
            for second_out in range(9, start_second_out - 1, -1):

                if first_in % 2 == 0 and second_in % 2 != 0 and first_out % 2 == 0 and second_out % 2 != 0:
                    if first_in == first_out and second_in == second_out:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first_in}{second_in} - {first_out}{second_out}")
                        counter += 1
                        if counter == 6:
                            is_enough = True
                            break
            if is_enough:
                break
        if is_enough:
            break
    if is_enough:
        break