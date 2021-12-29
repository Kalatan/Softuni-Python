film_name = input()
ticket_count = 0
total_tickets = 0
standard_count = 0
student_count = 0
kid_count = 0
total_standard_count = 0
total_student_count = 0
total_kid_count = 0
is_finish = False

while film_name != "Finish":
    capacity = int(input())
    ticket_type = input()
    while ticket_type != "End":
        ticket_count += 1
        if ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "student":
            student_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        if ticket_count == capacity:
            break
        ticket_type = input()

    print(f"{film_name} - {100 * (ticket_count / capacity):.2f}% full.")

    total_tickets += ticket_count
    total_standard_count += standard_count
    total_student_count += student_count
    total_kid_count += kid_count

    ticket_count = 0
    standard_count = 0
    student_count = 0
    kid_count = 0
    film_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{100*(total_student_count / total_tickets):.2f}% student tickets.")
print(f"{100*(total_standard_count / total_tickets):.2f}% standard tickets.")
print(f"{100*(total_kid_count / total_tickets):.2f}% kids tickets.")
