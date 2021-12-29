numbers_group = int(input())
sum_odd = 0
sum_even = 0

for n in range(1, numbers_group + 1):
    if n % 2 == 1:
        odd_group = int(input())
        sum_odd += odd_group
    elif n % 2 == 0:
        even_group = int(input())
        sum_even += even_group

if sum_odd == sum_even:
    print(f"Yes\n"
          f"Sum = {sum_odd}")
elif sum_odd != sum_even:
    difference = abs(sum_odd - sum_even)
    print(f"No\n"
          f"Diff = {difference}")