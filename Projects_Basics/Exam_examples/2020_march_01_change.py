bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

bitcoin_leva = bitcoin_count * 1168
yuan_leva = (yuan_count * 0.15) * 1.76

total_leva = bitcoin_leva + yuan_leva
total_euro = total_leva / 1.95
total = total_euro - (total_euro * (commission * 0.01))
print(f"{total:.2f}")
