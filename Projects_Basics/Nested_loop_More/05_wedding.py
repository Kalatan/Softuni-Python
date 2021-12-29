men_count = int(input())
women_count = int(input())
max_tables = int(input())
count_tables = 0

for man in range(1, men_count + 1):
    for woman in range(1, women_count + 1):
        count_tables += 1
        if count_tables <= max_tables:
            print(f"({man} <-> {woman})", end=" ")
