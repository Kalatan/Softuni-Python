computer_models = int(input())
total_sells = 0
total_rating = 0

for model in range(1, computer_models + 1):
    command = int(input())
    string_command = str(command)
    rating = int(string_command[2])
    possible_sells = int(string_command[0] + string_command[1])

    if rating == 2:
        sells = 0
    elif rating == 3:
        sells = possible_sells * 0.5
    elif rating == 4:
        sells = possible_sells * 0.7
    elif rating == 5:
        sells = possible_sells * 0.85
    elif rating == 6:
        sells = possible_sells

    total_sells += sells
    total_rating += rating

average_rating = total_rating / computer_models

print(f"{total_sells:.2f}")
print(f"{average_rating:.2f}")
