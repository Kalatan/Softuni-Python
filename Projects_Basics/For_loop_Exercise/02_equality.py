import sys

number = int(input())
sum = 0
max_num = -sys.maxsize

for n in range(1, number + 1):
    number = int(input())
    sum += number
    if number > max_num:
        max_num = number
if max_num == sum - max_num:
    print((f"Yes\n"
           f"Sum = {sum - max_num}"))
else:
    dif = abs(max_num - (sum - max_num))
    print((f"No\n"
           f"Diff = {dif}"))
