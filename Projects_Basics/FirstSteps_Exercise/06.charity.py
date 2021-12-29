days_count = int(input())
cook_count = int(input())
cake_count = int(input())
gof_count = int(input())
pancake_count = int(input())

cake_price = float(45)
gof_price = float(5.8)
pancake_price = float(3.2)

total_cake_count = cake_count * days_count * cook_count
total_gof_count = gof_count * days_count * cook_count
total_pancake_count = pancake_count * days_count * cook_count

total_cake_price = cake_price * total_cake_count
total_gof_price = gof_price * total_gof_count
total_pancake_price = pancake_price * total_pancake_count

revenue = total_cake_price + total_gof_price + total_pancake_price
expenses = (total_cake_price + total_gof_price + total_pancake_price)/ 8

charity = revenue - expenses

print(charity)
