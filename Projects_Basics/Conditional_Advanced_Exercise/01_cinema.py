type_movie = input()
rows = int(input())
columns = int(input())
total_places = rows * columns
price = 0

if type_movie == "Premiere":
    price = 12
elif type_movie == "Normal":
    price = 7.5
elif type_movie == "Discount":
    price = 5

income = total_places * price
print(f"{income:.2f} leva")
