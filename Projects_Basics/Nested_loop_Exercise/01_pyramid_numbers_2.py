number = int(input())
counter = 0
is_bigger = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        counter += 1
        if counter <= number:
            print(counter, end=" ")
        else:
            is_bigger = True
            break
    if is_bigger:
        break
    else:
        print()