destination = input()
needed_budget = float(input())
saved_money = 0

while destination != "End":

    while saved_money < needed_budget:
        saving_money = float(input())
        saved_money += saving_money
    else:
        print(f"Going to {destination}!")
        destination = input()
        saved_money = 0
        if destination == "End":
            break
        needed_budget = float(input())