main_number = int(input())
number = int(input())
sum = number
while sum < main_number:
    number = int(input())
    sum += number
print(sum)