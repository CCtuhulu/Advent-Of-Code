import math
import matplotlib.path as mpath
import matplotlib.pyplot as plt

with open("Day 10 - Pipe Maze\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


polygon_path = []
#FIND THE S POSITION
for y, line in enumerate(lines):
    found = False
    for x, chr in enumerate(line):
        if chr == 'S':
            S = (x,y)
            found = True
            break

    if found:
        break

#Finding starting and ending positions
start_found = False
if lines[S[1]-1][S[0]] == '|' or lines[S[1]-1][S[0]] == '7' or lines[S[1]-1][S[0]] == 'F':
    start_pos = (S[0], S[1]-1)
    start_found = True

if lines[S[1]+1][S[0]] == '|' or lines[S[1]+1][S[0]] == 'J' or lines[S[1]+1][S[0]] == 'L':
    if start_found:
        end_pos = (S[0], S[1]+1)
    else:
        start_pos = (S[0], S[1]+1)
    start_found = True

if lines[S[1]][S[0]-1] == '-' or lines[S[1]+1][S[0]] == 'L' or lines[S[1]+1][S[0]] == 'F':
    if start_found:
        end_pos = (S[0]-1, S[1])
    else:
        start_pos = (S[0]-1, S[1])    
    start_found = True   

if lines[S[1]][S[0]-1] == '-' or lines[S[1]+1][S[0]] == '7' or lines[S[1]+1][S[0]] == 'J':
    if start_found:
        end_pos = (S[0]+1, S[1])
    else:
        start_pos = (S[0]+1, S[1])  


#Counting the number of letters between start and end
current_pos = start_pos
last_pos = S
polygon_path.append(S)
polygon_path.append(start_pos)

while current_pos != end_pos:

    sign = lines[current_pos[1]][current_pos[0]]
    
    if sign == '|':
        temp = current_pos

        if current_pos[1]+1 != last_pos[1]:
            current_pos = (current_pos[0],current_pos[1]+1)
        else:
            current_pos = (current_pos[0],current_pos[1]-1)
        
        last_pos = temp

    elif sign == '-':
        temp = current_pos

        if current_pos[0]-1 != last_pos[0]:
            current_pos = (current_pos[0]-1,current_pos[1])
        else:
            current_pos = (current_pos[0]+1,current_pos[1])
        
        last_pos = temp
    
    elif sign == 'L':
        temp = current_pos

        if current_pos[1]-1 != last_pos[1]:
            current_pos = (current_pos[0],current_pos[1]-1)
        else:
            current_pos = (current_pos[0]+1,current_pos[1])
        
        last_pos = temp

    elif sign == 'J':
        temp = current_pos

        if current_pos[1]-1 != last_pos[1]:
            current_pos = (current_pos[0],current_pos[1]-1)
        else:
            current_pos = (current_pos[0]-1,current_pos[1])
        
        last_pos = temp

    elif sign == '7':
        temp = current_pos

        if current_pos[1]+1 != last_pos[1]:
            current_pos = (current_pos[0],current_pos[1]+1)
        else:
            current_pos = (current_pos[0]-1,current_pos[1])
        
        last_pos = temp

    elif sign == 'F':
        temp = current_pos

        if current_pos[1]+1 != last_pos[1]:
            current_pos = (current_pos[0],current_pos[1]+1)
        else:
            current_pos = (current_pos[0]+1,current_pos[1])
        
        last_pos = temp

    polygon_path.append(current_pos)


points_inside = 0
polygon = mpath.Path(polygon_path)

for row in range(len(lines)):
    for column in range(len(lines[0])):
        if polygon.contains_point((row,column)) and not((row,column) in polygon_path):
            points_inside += 1

print(points_inside)
