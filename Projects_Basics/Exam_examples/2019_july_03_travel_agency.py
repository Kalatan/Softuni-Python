town = input()
package = input()
vip_discount = input()
days = int(input())
day_price = 0
is_invalid = False

if days > 0:
    if town == "Bansko" or town == "Borovets":
        if package == "withEquipment":
            day_price = 100
            if vip_discount == "yes":
                day_price *= 0.9
            elif vip_discount == "no":
                pass
        elif package == "noEquipment":
            day_price = 80
            if vip_discount == "yes":
                day_price *= 0.95
            elif vip_discount == "no":
                pass
        else:
            is_invalid = True
    elif town == "Varna" or town == "Burgas":
        if package == "withBreakfast":
            day_price = 130
            if vip_discount == "yes":
                day_price *= 0.88
            elif vip_discount == "no":
                pass
        elif package == "noBreakfast":
            day_price = 100
            if vip_discount == "yes":
                day_price *= 0.93
            elif vip_discount == "no":
                pass
        else:
            is_invalid = True
    else:
        is_invalid = True

    if is_invalid:
        print("Invalid input!")
    else:
        if days > 7:
            print(f"The price is {(day_price * (days - 1)):.2f}lv! Have a nice time!")
        else:
            print(f"The price is {(day_price * days):.2f}lv! Have a nice time!")

elif days <= 0:
    print("Days must be positive number!")




