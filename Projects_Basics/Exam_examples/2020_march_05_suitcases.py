capacity = float(input())
suitcase = input()
volume = 0
count_suitcase = 0
counter = 0
is_finished = False

while suitcase != "End":
    suitcase = float(suitcase)
    counter += 1
    if counter % 3 == 0:
        suitcase *= 1.1
    volume += suitcase
    if volume <= capacity:
        count_suitcase += 1
        suitcase = input()
    else:
        is_finished = True
        break

if is_finished:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_suitcase} suitcases loaded.")
