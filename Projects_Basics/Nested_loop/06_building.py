floor_count = int(input())
rooms_floor_count = int(input())

for floor in range(floor_count, 0, -1):
    for room in range(0, rooms_floor_count):
        if floor == floor_count:
            print(f"L{floor}{room}", end=" ") # искаме да принтираме номерата на стаите на същия ред
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
        else:
            print(f"A{floor}{room}", end=" ")
    print() # Минаваме на нов ред след като минем през всички стаи на един етаж