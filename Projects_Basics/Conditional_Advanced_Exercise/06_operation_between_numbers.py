number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
odd_even = ""

if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2
elif operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
    else:
        print(f"Cannot divide {number_1} by zero")
elif operator == "%":
    if number_2 != 0:
        result = number_1 % number_2
    else:
        print(f"Cannot divide {number_1} by zero")

if result % 2 == 0:
    odd_even = "even"
else:
    odd_even = "odd"

if (operator == "/" or operator == "%") and number_2 == 0:
    pass
else:
    if operator == "+" or operator == "-" or operator == "*":
        print(f"{number_1} {operator} {number_2} = {result} - {odd_even}")
    elif operator == "/":
        print(f"{number_1} / {number_2} = {result:.2f}")
    elif operator == "%":
        print(f"{number_1} % {number_2} = {result}")
