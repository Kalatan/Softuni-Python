lenght = int(input())
width = int(input())
height = int(input())
taken_volume_perc = (float(input()))/100

aquarium_volume = (0.1 * lenght) * (0.1 * width) * (0.1 * height)
left_volume = aquarium_volume - aquarium_volume * taken_volume_perc

print(left_volume)
