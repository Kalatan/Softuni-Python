start_range = int(input())
end_range = int(input())

string_start = str(start_range)
string_end = str(end_range)

start_first = string_start[0]
start_second = string_start[1]
start_third = string_start[2]
start_fourth = string_start[3]

end_first = string_end[0]
end_second = string_end[1]
end_third = string_end[2]
end_fourth = string_end[3]

for first in range(int(start_first), int(end_first) + 1):
    is_even = False
    if first % 2 == 0:
        continue
    else:
        for second in range(int(start_second), int(end_second) + 1):
            if second % 2 == 0:
                continue
            else:
                for third in range(int(start_third), int(end_third) + 1):
                    if third % 2 == 0:
                        continue
                    else:
                        for fourth in range(int(start_fourth), int(end_fourth) + 1):
                            if fourth % 2 == 0:
                                continue
                            else:
                                print(f"{first}{second}{third}{fourth}", end=" ")
