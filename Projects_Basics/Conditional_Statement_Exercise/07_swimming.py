current_record = float(input())
distance = float(input())
speed = float(input())

slowing = (distance // 15) * 12.5

swim_time = distance * speed + slowing

if swim_time < current_record:
    print(f" Yes, he succeeded! The new world record is {swim_time:.2f} seconds.")
elif swim_time >= current_record:
    needed_seconds = swim_time - current_record
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")