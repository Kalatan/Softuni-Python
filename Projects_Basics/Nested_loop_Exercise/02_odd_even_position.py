first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_sum = 0
    even_sum = 0
    current_number_string = str(current_number)
    for index, digit in enumerate(current_number_string):
        if index % 2 == 0:
            odd_sum += int(digit) # понеже индексите започват да броят от 0, а не от 1, на четните индексите се намират нечетните видими позиции и обратното
        else:
            even_sum += int(digit)
        if even_sum == odd_sum:
            print(current_number, end=" ")