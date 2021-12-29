w = int(input())
d = int(input())
h = int(input())
text = input()
room_volume = w * d * h
sum_boxes = 0

while text != "Done":
    boxes = int(text)
    sum_boxes += boxes
    if sum_boxes > room_volume:
        break
    text = input()

if sum_boxes > room_volume:
    print(f"No more free space! You need {sum_boxes - room_volume} Cubic meters more.")
else:
    print(f"{room_volume - sum_boxes} Cubic meters left.")