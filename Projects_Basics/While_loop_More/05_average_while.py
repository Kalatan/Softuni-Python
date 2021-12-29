input_num = int(input())
counter = 0
numbers_sum = 0
average = 0


while counter < input_num:
    numbers = int(input())
    counter += 1
    numbers_sum += numbers
    average = numbers_sum / counter

print(f"{average:.2f}")
