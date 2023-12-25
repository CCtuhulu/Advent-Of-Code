
with open('Day 2 - I Was Told There Would Be No Math\input.txt', 'r') as file:
    lines = file.readlines()

result = 0
for line in lines:
    measures = line.split('x')
    result += 2 * int(measures[0]) * int(measures[1]) + 2 * int(measures[0]) * int(measures[2]) + 2 * int(measures[1]) * int(measures[2])
    m = min(int(measures[0]) * int(measures[1]), int(measures[0]) * int(measures[2]), int(measures[1]) * int(measures[2]))
    result += m

print(result)