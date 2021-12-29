groups_count = int(input())
mount_1 = 0
mount_2 = 0
mount_3 = 0
mount_4 = 0
mount_5 = 0

for group in range(1, groups_count + 1):
    climbers = int(input())
    if climbers <= 5:
        mount_1 += climbers
    elif 6 <= climbers <= 12:
        mount_2 += climbers
    elif 13 <= climbers <= 25:
        mount_3 += climbers
    elif 26 <= climbers <= 40:
        mount_4 += climbers
    elif 41 <= climbers:
        mount_5 += climbers

total = mount_1 + mount_2 + mount_3 + mount_4 + mount_5

print(f"{(mount_1 / total) * 100:.2f}%")
print(f"{(mount_2 / total) * 100:.2f}%")
print(f"{(mount_3 / total) * 100:.2f}%")
print(f"{(mount_4 / total) * 100:.2f}%")
print(f"{(mount_5 / total) * 100:.2f}%")