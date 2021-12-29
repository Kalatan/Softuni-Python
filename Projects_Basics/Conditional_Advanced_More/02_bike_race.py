junior_count = int(input())
senior_count = int(input())
track_type = input()

tax = 0

if track_type == "trail":
    tax = junior_count * 5.5 + senior_count * 7
elif track_type == "cross-country":
    tax = junior_count * 8 + senior_count * 9.5
    if junior_count + senior_count >= 50:
        tax *= 0.75
elif track_type == "downhill":
    tax = junior_count * 12.25 + senior_count * 13.75
elif track_type == "road":
    tax = junior_count * 20 + senior_count * 21.5

tax *= 0.95

print(f"{tax:.2f}")