import math

record_seconds = float(input())
distance = float(input())
time_per_meter = float(input())

run_seconds = distance * time_per_meter
bonus_seconds = math.floor(distance / 50) * 30
total_seconds = run_seconds + bonus_seconds

if total_seconds < record_seconds:
    print(f"Yes! The new record is {total_seconds:.2f} seconds.")
else:
    print(f"No! He was {(total_seconds - record_seconds):.2f} seconds slower.")