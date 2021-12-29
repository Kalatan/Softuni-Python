numbers_group = int(input())
sum_left = 0
sum_right = 0

for n in range(1, numbers_group + 1):
    first_group = int(input())
    sum_left += first_group
for n in range(numbers_group + 1, numbers_group * 2 + 1):
    second_group = int(input())
    sum_right += second_group

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
elif sum_left != sum_right:
    difference = abs(sum_left - sum_right)
    print(f"No, diff = {difference}")
