name = input()
tickets_count_adult = int(input())
tickets_count_child = int(input())
tickets_price = float(input())
service_price = float(input())

tickets_adult_price = tickets_price + service_price
tickets_child_price = tickets_price * 0.3 + service_price

total_adult_profit = tickets_count_adult * tickets_adult_price
total_child_profit = tickets_count_child * tickets_child_price
total_profit = (total_adult_profit + total_child_profit) * 0.2

print(f"The profit of your agency from {name} tickets is {total_profit:.2f} lv.")