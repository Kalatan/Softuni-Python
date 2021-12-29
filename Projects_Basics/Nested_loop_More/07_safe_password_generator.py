x_range = int(input())
y_range = int(input())
max_passwords = int(input())
count_passwords = 0

second_range = 63
fourth_range = 0

for first in range(35, 56):
    second_range += 1
    for second in range(second_range, 97):
        for third in range(1, x_range + 1):
            fourth_range += 1
            for fourth in range(fourth_range, y_range + 1):
                count_passwords += 1
                if count_passwords <= max_passwords:
                    print(f"{chr(first)}{chr(second)}{third}{fourth}{chr(second)}{chr(first)}")
                else:
                    break
                break
            break
        break