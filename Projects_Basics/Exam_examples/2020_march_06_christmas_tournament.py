days = int(input())

dayly_won_money = 0
total_won_money = 0
total_won_games = 0
total_lost_games = 0

for day in range(1, days + 1):
    sport = input()
    won_money = 0
    won_games = 0
    lost_games = 0

    while sport != "Finish":
        result = input()
        if result == "win":
            won_games += 1
            won_money += 20
        elif result == "lose":
            lost_games += 1
        sport = input()

    if won_games > lost_games:
        dayly_won_money = won_money * 1.1
    else:
        dayly_won_money = won_money

    total_won_money += dayly_won_money
    total_won_games += won_games
    total_lost_games += lost_games

if total_won_games > total_lost_games:
    total_won_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_won_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_won_money:.2f}")