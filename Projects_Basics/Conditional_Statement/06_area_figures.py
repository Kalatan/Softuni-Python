from math import pi

figure = input()

if figure == "square":
    s_side = float(input())
    s_area = s_side ** 2
    print(f"{s_area:.3f}")
elif figure == "rectangle":
    r_side_1 = float(input())
    r_side_2 = float(input())
    print(f"{(r_side_1 * r_side_2):.3f}")
elif figure == "circle":
    radius = float(input())
    c_area = pi * (radius ** 2)
    print(f"{c_area:.3f}")
elif figure == "triangle":
    t_side = float(input())
    t_h = float(input())
    print(f"{(t_side * t_h)/2:.3f}")
