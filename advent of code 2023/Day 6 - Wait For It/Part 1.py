import re

with open('Day 6 - Wait For It\input.txt', 'r') as file:
    lines = file.readlines()

times = [int(time) for time in re.findall(r'(\d+)',lines[0])]
distances = [int(distance) for distance in re.findall(r'(\d+)',lines[1])]

points = 1

for time, distance in zip(times,distances):
    
    winnings = 0

    for t in range(time):
        distance_travelled = (time-t) * t

        if distance_travelled > distance:
            winnings += 1

    points *= winnings

print(points)