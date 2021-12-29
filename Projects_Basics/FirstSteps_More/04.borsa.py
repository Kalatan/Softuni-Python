from decimal import Decimal

vegetables_price = float(input())
fruits_price =  float(input())
vegetables_amount =  int(input())
fruits_amount =  int(input())

vegetables_total = vegetables_price * vegetables_amount / 1.94
fruits_total = fruits_price * fruits_amount / 1.94

total = Decimal(vegetables_total + fruits_total)

print(round(total, 2))

