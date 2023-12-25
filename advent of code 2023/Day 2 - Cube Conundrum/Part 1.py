import re


with open('Day 2 - Cube Conundrum\input.txt', 'r') as file:
    lines = file.readlines()


i = 0
parts = []
sum = 0


for line in lines:
    possible = True

    #cleaning the string
    parts.clear()
    removed_string = "Game " + str(i+1) + ":"
    line = line.replace(removed_string,"")
    parts = line.split(";")

    #checking
    for part in parts:
        matches = re.findall(r'(\d+) (\w+)', part)

        for match in matches: 
            if match[1] == "red" and int(match[0]) > 12:
                possible = False
            elif match[1] == "blue" and int(match[0]) > 14:
                possible = False
            elif match[1] == "green" and int(match[0]) > 13:
                possible = False

    if possible:
        sum += i+1

    i += 1

print(sum)