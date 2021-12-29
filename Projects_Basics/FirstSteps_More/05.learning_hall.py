h = float(input())
w = float(input())

h_spaces = h // 1.2
w_spaces = (w - 1) // 0.7

avaliable_area = int((h_spaces * w_spaces) - 3)

print(avaliable_area)