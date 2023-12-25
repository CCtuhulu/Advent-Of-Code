import re

with open('Day 2 - I Was Told There Would Be No Math\input.txt', 'r') as file:
    lines = file.readlines()

result = 0
for line in lines:
    measures = [int(digit) for digit in re.findall(r'(\d+)', line)]
    
    measures.sort()
    result += 2 * (measures[0]+measures[1]) + measures[0]*measures[1]*measures[2]

print(result)