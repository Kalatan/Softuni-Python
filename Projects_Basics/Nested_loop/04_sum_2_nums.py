start = int(input())
end = int(input())
number = int(input())

n1 = start
n2 = start
count_combinations = 0
is_combine = False

for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        count_combinations += 1
        if n1 + n2 == number:
            print(f"Combination N:{count_combinations} ({n1} + {n2} = {number})")
            is_combine = True
            break
    if is_combine:
        break

if is_combine is False:
    print(f"{count_combinations} combinations - neither equals {number}")