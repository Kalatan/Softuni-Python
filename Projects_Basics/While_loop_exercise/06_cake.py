w = int(input())
d = int(input())
cakes_text = input()

cake_size = w * d
cakes_count = 0

while cakes_text != "STOP":
    cakes_count += int(cakes_text)
    if cakes_count > cake_size:
        print(f"No more cake left! You need {cakes_count - cake_size} pieces more.")
        break
    cakes_text = input()

if cakes_text == "STOP":
    print(f"{cake_size - cakes_count} pieces are left.")
