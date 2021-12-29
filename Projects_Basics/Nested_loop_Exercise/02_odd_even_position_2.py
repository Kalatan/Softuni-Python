first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    string_of_number = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(string_of_number):
        number_of_digit = int(digit)
        if index == 0 or index % 2 == 0: # понеже индексите започват да броят от 0, а не от 1, на четните индексите се намират нечетните видими позиции и обратното
            odd_sum += number_of_digit
        else:
            even_sum += number_of_digit
    if odd_sum == even_sum:
        print(number, end=" ")