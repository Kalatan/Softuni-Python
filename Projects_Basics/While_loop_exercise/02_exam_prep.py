bad_grade_limit = int(input())
task_name = input()
grade = int(input())

grade_count = 0
grade_sum = 0
average_grade = 0
bad_grade_count = 0
bad_grade_reached = False
last_task_name = task_name

while task_name != "Enough":
    grade_count += 1
    grade_sum += grade
    average_grade = grade_sum / grade_count
    last_task_name = task_name
    if grade <= 4:
        bad_grade_count += 1
        if bad_grade_count == bad_grade_limit:
            bad_grade_reached = True
            print(f"You need a break, {bad_grade_count} poor grades.")
            break
    task_name = input()
    if task_name != "Enough":
        grade = int(input())

if bad_grade_reached is False:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grade_count}")
    print(f"Last problem: {last_task_name}")