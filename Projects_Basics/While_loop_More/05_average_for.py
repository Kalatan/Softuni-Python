n = int(input())
sum = 0
average = 0
count = 0

for i in range(1, n + 1):
    n = int(input())
    sum += n
    count += 1

average = sum / count
print(f"{average:.2f}")