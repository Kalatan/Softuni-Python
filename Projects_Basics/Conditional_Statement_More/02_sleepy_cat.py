off_days = int(input())

year = 365
work_days = year - off_days
sleep_norm = 30000  # min per year
work_day_play = 63
off_day_play = 127

sum_play_min = work_day_play * work_days + off_day_play * off_days

if sum_play_min > sleep_norm:
    excess_h = (sum_play_min - sleep_norm) // 60
    excess_m = (sum_play_min - sleep_norm) % 60
    print("Tom will run away")
    print(f"{excess_h} hours and {excess_m} minutes more for play")
else:
    needed_h = (sleep_norm - sum_play_min) // 60
    needed_m = (sleep_norm - sum_play_min) % 60
    print("Tom sleeps well")
    print(f"{needed_h} hours and {needed_m} minutes less for play")
