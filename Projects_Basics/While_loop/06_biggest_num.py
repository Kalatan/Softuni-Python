import sys
text = input()
max_number = -sys.maxsize

while text != "Stop":
    number = int(text)
    if number > max_number:
        max_number = number
    text = input()

print(max_number)