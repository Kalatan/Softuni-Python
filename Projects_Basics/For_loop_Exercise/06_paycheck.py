number_count = int(input())
paycheck = int(input())

for n in range(1, number_count + 1):
    website = input()
    if website == "Facebook":
        paycheck -= 150
    elif website == "Instagram":
        paycheck -= 100
    elif website == "Reddit":
        paycheck -= 50

if paycheck > 0:
    print(paycheck)
else:
    print("You have lost your salary.")


