last_sector = input()
rows_sector_a = int(input())
seat_odd_row = int(input())

last_sector_ord = ord(last_sector)
count_rows = rows_sector_a
count_odd_seats = 0
count_even_seats = 0

for sector in range(65, last_sector_ord + 1):
    count_rows += 1
    for row in range(1, count_rows):
        if row % 2 != 0:
            for seat_odd in range(97, 97 + seat_odd_row):
                count_odd_seats += 1
                print(f"{chr(sector)}{row}{chr(seat_odd)}")
        else:
            for seat_even in range(97, 97 + seat_odd_row + 2):
                count_even_seats += 1
                print(f"{chr(sector)}{row}{chr(seat_even)}")
print(count_odd_seats + count_even_seats)