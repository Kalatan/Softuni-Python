import sys
number_count = int(input())
max_print = -sys.maxsize
min_print = sys.maxsize

for n in range(0, number_count):
    number = int(input())
    if number < min_print:
        min_print = number
    if number > max_print:
        max_print = number

print(f"Max number: {max_print}")
print(f"Min number: {min_print}")

