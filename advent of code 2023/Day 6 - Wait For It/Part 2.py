import re

with open('Day 6 - Wait For It\input.txt', 'r') as file:
    lines = file.readlines()

times = re.findall(r'(\d+)',lines[0])
distances = re.findall(r'(\d+)',lines[1])

real_time =  int(''.join(times))
real_distance = int(''.join(distances)) 

points = 0

for t in range(real_time):
    distance_travelled = (real_time-t) * t

    if distance_travelled > real_distance:
        points += 1


print(points)