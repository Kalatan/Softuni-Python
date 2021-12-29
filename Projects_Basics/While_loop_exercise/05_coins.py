sum = float(input())
sum_int = int(sum * 100)
coins_count = 0

coins_count += sum_int // 200 # почваме от 200, защото това е равно на най-голямата монета - 2лв.
sum_int %= 200 # с това ще ни върне остатъка и след това него ще го ползваме в по-нататъпни проверки
coins_count += sum_int // 100
sum_int %= 100
coins_count += sum_int // 50
sum_int %= 50
coins_count += sum_int // 20
sum_int %= 20
coins_count += sum_int // 10
sum_int %= 10
coins_count += sum_int // 5
sum_int %= 5
coins_count += sum_int // 2
sum_int %= 2
coins_count += sum_int // 1
sum_int %= 1

print(coins_count)