import re

with open('Day 3 - Gear Ratios\input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for i in range(len(lines)):
    adjacent_numbers = []

    matches = re.finditer(r'\*', lines[i])

    for match in matches:
        
        adjacent_numbers.clear()

        #check line on top
        if i != 0:
            matches_top = re.finditer(r'(\d+)', lines[i-1])

            for match_n in matches_top:
                if match_n.start()-1 <= match.start() <= match_n.end():
                    adjacent_numbers.append(match_n.group())

        #check line after
        if i != len(lines)-1:
            matches_bot = re.finditer(r'(\d+)', lines[i+1])

            for match_n in matches_bot:
                if match_n.start()-1 <= match.start() <= match_n.end():
                    adjacent_numbers.append(match_n.group())

        #check current line
        matches_current = re.finditer(r'(\d+)', lines[i])
        for match_n in matches_current:
                if match_n.end() == match.start():
                    adjacent_numbers.append(match_n.group())

                if match_n.start() == match.end():
                    adjacent_numbers.append(match_n.group())


        if len(adjacent_numbers) == 2:
            sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
        
print(sum)