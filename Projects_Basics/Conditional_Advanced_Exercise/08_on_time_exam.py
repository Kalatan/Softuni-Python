exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

difference = abs(exam_time_in_minutes - arrival_time_in_minutes)
print_hour = difference // 60
print_minute = difference % 60
str_print_minute = str(print_minute)

if exam_time_in_minutes > arrival_time_in_minutes + 30:
    print("Early")
    if difference >= 60:
        print(f"{print_hour}:{str_print_minute.zfill(2)} hours before the start")
    else:
        print(f"{print_minute} minutes before the start")
elif 0 <= exam_time_in_minutes - arrival_time_in_minutes <= 30:
    print("On time")
    if difference == 0:
        pass
    else:
        print(f"{print_minute} minutes before the start")
elif exam_time_in_minutes < arrival_time_in_minutes:
    print("Late")
    if difference >= 60:
        print(f"{print_hour}:{str_print_minute.zfill(2)} hours after the start")
    else:
        print(f"{print_minute} minutes after the start")