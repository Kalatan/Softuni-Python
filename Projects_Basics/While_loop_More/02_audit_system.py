needed_money = int(input())
cash_pay = ""
card_pay = ""

collected_money = 0
cash_count = 0
cash_sum = 0
card_count = 0
card_sum = 0
ended = False

while needed_money > collected_money:
    cash_pay = input()
    if cash_pay != "End":
        card_pay = input()
        if int(cash_pay) > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash_count += 1
            cash_sum += int(cash_pay)

        if int(card_pay) < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card_count += 1
            card_sum += int(card_pay)

        collected_money = 0
        collected_money = cash_sum + card_sum

    else:
        ended = True
        break

if ended:
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {cash_sum / cash_count:.2f}")
    print(f"Average CC: {card_sum / card_count:.2f}")