volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
time = float(input())

pipe_1_water = pipe_1 * time
pipe_2_water = pipe_2 * time

total_water = pipe_1_water + pipe_2_water
pool_fill = total_water / volume * 100
pipe_1_water_perc = pipe_1_water / total_water * 100
pipe_2_water_perc = pipe_2_water / total_water * 100

if total_water <= volume:
    print(f"The pool is {pool_fill:.2f}% full. Pipe 1: {pipe_1_water_perc:.2f}%. Pipe 2: {pipe_2_water_perc:.2f}%.")
else:
    print(f"For {time:.2f} hours the pool overflows with {total_water - volume:.2f} liters.")
