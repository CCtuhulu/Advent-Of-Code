

with open('Day 1 - Trebuchet\input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    first = -1
    last = -1

    for character in line:
        if character.isdigit() and first == -1:
            first = int(character)
        elif character.isdigit() and first != -1:
            last = int(character)

    if last == -1:
        last = first

    concatenated_number = str(first) + str(last)
    sum += int(concatenated_number)

print(sum)