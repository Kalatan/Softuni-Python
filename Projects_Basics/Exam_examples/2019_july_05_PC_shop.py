games_sold = int(input())
total_games = 0
count_hearth = 0
count_fornite = 0
count_overwatch = 0
count_others = 0

for game in range(1, games_sold + 1):
    game_name = input()
    total_games += 1
    if game_name == "Hearthstone":
        count_hearth += 1
    elif game_name == "Fornite":
        count_fornite += 1
    elif game_name == "Overwatch":
        count_overwatch += 1
    else:
        count_others += 1

print(f"Hearthstone - {100 * (count_hearth / total_games):.2f}%")
print(f"Fornite - {100 * (count_fornite / total_games):.2f}%")
print(f"Overwatch - {100 * (count_overwatch / total_games):.2f}%")
print(f"Others - {100 * (count_others / total_games):.2f}%")