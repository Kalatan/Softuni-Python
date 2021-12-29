string = input()
value = 0

for char in string:
    v = 0
    if char == "a":
        v = 1
    elif char == "e":
        v = 2
    elif char == "i":
        v = 3
    elif char == "o":
        v = 4
    elif char == "u":
        v = 5
    value += v

print(value)
