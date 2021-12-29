voucher_price = int(input())
product = input()
tickets = 0
other_stuff = 0
product_price = 0
total = 0

while product != "End":
    if len(product) > 8:
        product_price = ord(product[0]) + ord(product[1])
        total += product_price

        if total <= voucher_price:
            tickets += 1
        else:
            break

    else:
        product_price = ord(product[0])
        total += product_price

        if total <= voucher_price:
            other_stuff += 1
        else:
            break

    product = input()

print(tickets)
print(other_stuff)