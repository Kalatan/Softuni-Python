trip_price = float(input())
start_money = float(input())

action = input()
action_sum = float(input())
sum = start_money
days_count = 1
spend_days_count = 0
got_money = False

while sum < trip_price:
    if action == "save":
        sum += action_sum
        if sum >= trip_price:
            got_money = True
            print(f"You saved the money for {days_count} days.")
            break
        spend_days_count = 0
    elif action == "spend":
        if action_sum >= sum:
            sum = 0
        else:
            sum -= action_sum
        spend_days_count += 1
        if spend_days_count == 5:
            print("You can't save the money.")
            print(days_count)
            break
    action = input()
    action_sum = float(input())
    days_count += 1

