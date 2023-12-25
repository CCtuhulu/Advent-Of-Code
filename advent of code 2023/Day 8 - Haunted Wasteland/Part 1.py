import re

with open('Day 8 - Haunted Wasteland\input.txt', 'r') as file:
    lines = file.readlines()


instructions = lines[0]
instructions = instructions[:-1]
instructions_index = 0

steps = 0


#putting everything in lists
route_list = []
for line in lines[2:]:
    source = line[0:3]
    left_destination = line[7:10]
    right_destination = line[12:15]
    route_list.append((source,left_destination,right_destination))


current_location = 'AAA'
current_index = -1

while current_location != 'ZZZ':

    #loop through instructions if we reach the end
    if(instructions_index > len(instructions)-1):
        instructions_index = 0

    for index, couple in enumerate(route_list):
        if current_location == couple[0]:
            current_index = index
            break

    if(instructions[instructions_index] == 'L'):
        current_location = route_list[current_index][1]

        for index, couple in enumerate(route_list):
            if current_location == couple[0]:
                current_index = index
                break


    else:
        current_location = route_list[current_index][2]
        
        for index, couple in enumerate(route_list):
            if current_location == couple[0]:
                current_index = index
                break


    steps += 1
    instructions_index += 1

print(steps)