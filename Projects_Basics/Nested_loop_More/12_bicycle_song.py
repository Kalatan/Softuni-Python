control_number = int(input())
counter = 0
magic_number = ""

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if (a * b) + (c * d) == control_number:
                            print(f"{a}{b}{c}{d}", end=" ")
                            counter += 1
                            if counter == 4:
                                magic_number = str(a) + str(b) + str(c) + str(d)
                    else:
                        break
        else:
            continue
print()
if counter >= 4:
    print(f"Password: {magic_number}")
else:
    print("No!")