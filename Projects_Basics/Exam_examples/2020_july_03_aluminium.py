windows_count = int(input())
windows_type = input()
delivery = input()
price = 0

if windows_count <= 10:
    print("Invalid order")
else:
    if windows_type == "90X130":
        price = 110
        if 30 < windows_count <= 60:
            price = 110 * 0.95
        elif windows_count > 60:
            price = 110 * 0.92
    elif windows_type == "100X150":
        price = 140
        if 40 < windows_count <= 80:
            price = 140 * 0.94
        elif windows_count > 80:
            price = 140 * 0.9
    elif windows_type == "130X180":
        price = 190
        if 20 < windows_count <= 50:
            price = 190 * 0.93
        elif windows_count > 50:
            price = 190 * 0.88
    elif windows_type == "200X300":
        price = 250
        if 25 < windows_count <= 50:
            price = 250 * 0.91
        elif windows_count > 50:
            price = 250 * 0.86

    total_window_price = price * windows_count

    if delivery == "With delivery":
        total_window_price += 60

    if windows_count > 99:
        total_window_price *= 0.96
    print(f"{total_window_price:.2f} BGN")
