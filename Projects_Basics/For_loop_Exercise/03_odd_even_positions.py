import sys
number_count = int(input())
odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize
even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize

for n in range(1, number_count + 1):
    number = float(input())
    if n % 2 == 1:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    elif n % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

print(f"OddSum={odd_sum:.2f},")
if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print(f"OddMin=No,")
if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print(f"EvenMin=No,")
if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMax=No")