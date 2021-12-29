name = input()
sum_grades = 0
excluded = 0
years = 1

while years <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1
        if excluded > 1:
            break
        continue
    sum_grades += grade
    average_grades = sum_grades / 12
    years += 1

if excluded > 1:
    print(f"{name} has been excluded at {years} grade")
else:
    print(f"{name} graduated. Average grade: {average_grades:.2f}")
