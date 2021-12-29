first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for a in range(1, first_limit + 1):
    if a % 2 == 0:
        for b in range(2, second_limit + 1):
            if b % 2 == 0 and b != 2:
                continue
            if b % 3 == 0 and b != 3:
                continue
            if b % 5 == 0 and b != 5:
                continue

            for c in range(1, third_limit + 1):
                if c % 2 == 0:
                    print(a, b, c)
    else:
        continue

