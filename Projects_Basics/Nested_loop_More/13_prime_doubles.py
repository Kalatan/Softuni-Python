first_double_start = int(input())
second_double_start = int(input())
first_double_limit = int(input())
second_double_limit = int(input())

for num_1 in range(first_double_start, first_double_start + first_double_limit + 1):
    is_prime_1 = True

    for n in range(2, num_1):
        if num_1 % n == 0:
            is_prime_1 = False
            break
    if is_prime_1:
        prime_num_1 = num_1
    else:
        continue

    for num_2 in range(second_double_start, second_double_start + second_double_limit + 1):
        is_prime_2 = True

        for m in range(2, num_2):
            if num_2 % m == 0:
                is_prime_2 = False
                break
        if is_prime_2:
            prime_num_2 = num_2

        if is_prime_1 and is_prime_2:
            string = str(prime_num_1) + str(prime_num_2)
            print(int(string))