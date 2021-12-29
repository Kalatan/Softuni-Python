player_name = input()
points = 0
player_points = 0
max_points = 0
winner = ""

while player_name != "Stop":
    for n in range(0, len(player_name)):
        number = int(input())

        letter_ord = ord(player_name[n])

        if letter_ord == number:
            points = 10
        else:
            points = 2

        player_points += points

    if player_points >= max_points:
        max_points = player_points
        winner = player_name
    player_name = input()
    player_points = 0

print(f"The winner is {winner} with {max_points} points!")
