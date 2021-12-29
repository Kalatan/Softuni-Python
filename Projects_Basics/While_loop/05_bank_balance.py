money_sent = input()
total_sum = 0

while money_sent != "NoMoreMoney":
    sum = float(money_sent)
    if sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {sum:.2f}")
        total_sum += sum
    money_sent = input()

print(f"Total: {total_sum:.2f}")
