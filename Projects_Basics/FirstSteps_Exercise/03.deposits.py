deposit = float(input())
term = int(input())
glp = (float(input())/100)

total = deposit + (term *((deposit * glp)/12))

print(total)