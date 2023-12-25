import re

with open("Day 6 - Probably a Fire Hazard\input.txt", 'r') as file:
    lines = file.readlines()

map = [[0 for j in range(1000)] for i in range(1000)]

for line in lines:

    coords = [int(coord) for coord in re.findall(r'(\d+)', line)]
    
    if 'turn on' in line:
        for i in range(coords[0], coords[2]+1):
            for j in range(coords[1], coords[3]+1):
                map[i][j] += 1

    elif 'turn off' in line:
        for i in range(coords[0], coords[2]+1):
            for j in range(coords[1], coords[3]+1):
                if map[i][j] != 0:
                    map[i][j] -= 1

    elif 'toggle' in line:
        for i in range(coords[0], coords[2]+1):
            for j in range(coords[1], coords[3]+1):
                map[i][j] += 2



total_brightness = 0

for m in map:
    total_brightness += sum(m)

print(total_brightness)