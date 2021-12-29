exam_students = int(input())
top = 0
upper = 0
middle = 0
bad = 0
sum_asses = 0

for student in range(1, exam_students + 1):
    assess = float(input())
    sum_asses += assess
    if assess >= 5:
        top += 1
    elif 4 <= assess < 5:
        upper += 1
    elif 3 <= assess < 4:
        middle += 1
    elif assess < 3:
        bad += 1

top_perc = top / exam_students * 100
upper_perc = upper / exam_students * 100
middle_perc = middle / exam_students * 100
bad_perc = bad / exam_students * 100
average = sum_asses / exam_students

print(f"Top students: {top_perc:.2f}%")
print(f"Between 4.00 and 4.99: {upper_perc:.2f}%")
print(f"Between 3.00 and 3.99: {middle_perc:.2f}%")
print(f"Fail: {bad_perc:.2f}%")
print(f"Average: {average:.2f}")
