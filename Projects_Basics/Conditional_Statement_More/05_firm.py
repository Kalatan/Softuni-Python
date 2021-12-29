import math
hours_needed = int(input())
days = int(input())
extra_workers = int(input())

work_days = 0.9 * days
work_hours = work_days * 8
extra_hours = extra_workers * days * 2

all_hours = math.floor(work_hours + extra_hours)

if all_hours >= hours_needed:
    print(f"Yes!{all_hours - hours_needed} hours left.")
else:
    print(f"Not enough time!{hours_needed - all_hours} hours needed.")
