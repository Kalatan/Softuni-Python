price_per_sqm = float(7.61)
discount = float(0.18)

area = float(input())
price = area * price_per_sqm
total_discount = price * discount
final_price = price - total_discount


print(f"The final price is: {final_price} lv.")
print(f"The discount is: {total_discount} lv.")
