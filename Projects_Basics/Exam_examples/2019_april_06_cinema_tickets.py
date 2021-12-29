film_name = input()
student_count = 0
standard_count = 0
kid_count = 0
total_ticket_count = 0

while film_name != "Finish":
    hall_seats = int(input())
    ticket_type = input()
    ticket_count = 0

    while ticket_type != "End":
        ticket_count += 1

        if ticket_count <= hall_seats:
            if ticket_type == "student":
                student_count += 1
            elif ticket_type == "standard":
                standard_count += 1
            elif ticket_type == "kid":
                kid_count += 1
        else:
            break

        if ticket_count == hall_seats:
            break

        ticket_type = input()

    print(f"{film_name} - {(ticket_count / hall_seats) * 100:.2f}% full.")
    total_ticket_count += ticket_count

    film_name = input()

print(f"Total tickets: {total_ticket_count}")
print(f"{(student_count / total_ticket_count) * 100:.2f}% student tickets.")
print(f"{(standard_count / total_ticket_count) * 100:.2f}% standard tickets.")
print(f"{(kid_count / total_ticket_count) * 100:.2f}% kids tickets.")

