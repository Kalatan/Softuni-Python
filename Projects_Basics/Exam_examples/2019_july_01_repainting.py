nailon = int(input())
paint = int(input())
substance = int(input())
hours = int(input())

total = (nailon + 2) * 1.5 + paint * 1.1 * 14.5 + substance * 5 + 0.4
work_hour = total * 0.3

total_expenses = total + hours * work_hour

print(f"Total expenses: {total_expenses:.2f} lv.")