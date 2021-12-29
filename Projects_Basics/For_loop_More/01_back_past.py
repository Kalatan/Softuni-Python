money_inherited = float(input())
target_year = int(input())
years = target_year - 1800
even_money_spent = 0
odd_money_spent = 0

for n in range(0, years + 1):
    if n % 2 == 0:
        even_money_spent += 12000
    elif n % 2 == 1:
        odd_money_spent += 12000 + (50 * (n + 18))

total = even_money_spent + odd_money_spent
dif = abs(money_inherited - total)

if money_inherited >= total:
    print(f"Yes! He will live a carefree life and will have {dif:.2f} dollars left.")
elif money_inherited < total:
    print(f"He will need {dif:.2f} dollars to survive.")