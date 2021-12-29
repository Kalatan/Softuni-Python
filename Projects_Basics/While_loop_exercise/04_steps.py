target_steps = 10000
total_steps = 0
going_home = False

while total_steps < target_steps:
    current_steps = input()
    if current_steps == "Going home":
        going_home = True
        break
    total_steps += int(current_steps)

if going_home:
    current_steps = int(input())
    total_steps += current_steps
diff = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")