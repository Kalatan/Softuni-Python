import sys

film_count = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
rating_sum = 0

for film in range(1, film_count + 1):
    film_name = input()
    rating = float(input())
    rating_sum += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_film = film_name
    if rating < min_rating:
        min_rating = rating
        min_rating_film = film_name

print(f"{max_rating_film} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_film} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {rating_sum / film_count:.1f}")