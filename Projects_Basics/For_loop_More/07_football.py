stadium = int(input())
fans_count = int(input())
section = ""
section_a = 0
section_b = 0
section_c = 0
section_d = 0

for fan in range(1, fans_count + 1):
    section = input()
    if section == "A":
        section_a += 1
    elif section == "B":
        section_b += 1
    elif section == "V":
        section_c += 1
    elif section == "G":
        section_d += 1

total_fans = section_a + section_b + section_c + section_d
section_a_perc = (section_a / total_fans) * 100
section_b_perc = (section_b / total_fans) * 100
section_c_perc = (section_c / total_fans) * 100
section_d_perc = (section_d / total_fans) * 100
total_perc = (total_fans / stadium) * 100

print(f"{section_a_perc:.2f}%")
print(f"{section_b_perc:.2f}%")
print(f"{section_c_perc:.2f}%")
print(f"{section_d_perc:.2f}%")
print(f"{total_perc:.2f}%")