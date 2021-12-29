book_name = input()
book_search = input()
book_count = 0

while book_search != "No More Books":
    if book_search == book_name:
        break
    book_count += 1
    book_search = input()

if book_search == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")
