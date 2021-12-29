x_range = int(input())
y_range = int(input())
max_passwords = int(input())
count_passwords = 0

first = 35
second = 64

for third in range(1, x_range + 1):
    for fourth in range(1, y_range + 1):
        count_passwords += 1
        if count_passwords <= max_passwords:
            if first == 56:
                first = 35
            if second == 97:
                second = 64
            print(f"{chr(first)}{chr(second)}{third}{fourth}{chr(second)}{chr(first)}", end="|")
            first += 1
            second += 1
        else:
            break
