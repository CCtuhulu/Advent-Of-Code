import re


with open('Day 2 - Cube Conundrum\input.txt', 'r') as file:
    lines = file.readlines()


i = 0
parts = []
sum = 0


for line in lines:
    min_green = -1
    min_blue = -1
    min_red = -1

    #cleaning the string
    removed_string = "Game " + str(i+1) + ":"
    matches = re.findall(r'(\d+) (\w+)', line)

    for match in matches:
        if match[1] == "red" and int(match[0]) > min_red:
                min_red = int(match[0])
        elif match[1] == "blue" and int(match[0]) > min_blue:
                min_blue = int(match[0])
        elif match[1] == "green" and int(match[0]) > min_green:
                min_green = int(match[0])

    sum += min_green * min_blue * min_red

print(sum)
