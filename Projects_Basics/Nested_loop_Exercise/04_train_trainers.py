jury = int(input())
presentation = input()
presentation_sum = 0
presentation_count = 0
average_sum = 0

while presentation != "Finish":
    for n in range(1, jury + 1):
        evaluation = float(input())
        presentation_sum += evaluation
    average = presentation_sum / jury
    presentation_count += 1
    print(f"{presentation} - {average:.2f}.")
    presentation = input()
    presentation_sum = 0
    average_sum += average
    total_average = average_sum / presentation_count
print(f"Student's final assessment is {total_average:.2f}.")

