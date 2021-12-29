start_interval = int(input())
end_interval = int(input())

for first in range(start_interval, end_interval + 1):
    for second in range(start_interval, end_interval + 1):
        for third in range(start_interval, end_interval + 1):

            if (second + third) % 2 == 0:
                for fourth in range(start_interval, end_interval + 1):
                    if fourth < first:
                        is_smaller = True
                        if (first % 2 == 0 and fourth % 2 != 0) or (first % 2 != 0 and fourth % 2 == 0):
                            print(f"{first}{second}{third}{fourth}", end=" ")

                    else:
                        is_smaller = False
                        break
            else:
                continue

            if not is_smaller:
                continue
        if not is_smaller:
            continue
    if not is_smaller:
        continue
