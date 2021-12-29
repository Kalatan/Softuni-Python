strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

bananas_price = 0.2 * (strawberry_price / 2)
oranges_price = 0.6 * (strawberry_price / 2)
raspberries_price = strawberry_price / 2
total = strawberries * strawberry_price + raspberries * raspberries_price + oranges * oranges_price + bananas * bananas_price

print(total)