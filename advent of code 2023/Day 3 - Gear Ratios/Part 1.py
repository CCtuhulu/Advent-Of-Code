import re


symbols = ['+', '/', '=', '@', '&', '$', '%', '-', '#', '*']

with open('Day 3 - Gear Ratios\input.txt', 'r') as file:
    lines = file.readlines()


sum = 0
for i in range(len(lines)):
    adjacent_list = []

    matches = re.finditer(r'(\d+)', lines[i])


    for match in matches:
        adjacent_list.clear()
        
        # create a list of all adjacent characters of numbers one by one
        for k,chr in enumerate(match.group()):
            index = match.start() + k

            if i == 0:
                if index == 0:
                    adjacent_list.append(lines[i][index+1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index+1])

                elif index == len(lines[i])-1:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index-1])

                else:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i][index+1])

                    adjacent_list.append(lines[i+1][index-1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index+1])

            elif i == len(lines)-1:
                if index == 0:
                    adjacent_list.append(lines[i][index+1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index+1])

                elif index == len(lines[i])-1:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index-1])

                else:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i][index+1])

                    adjacent_list.append(lines[i-1][index-1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index+1])
            else:
                if index == 0:
                    adjacent_list.append(lines[i][index+1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index+1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index+1])

                elif index == len(lines[i])-1:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index-1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index-1])

                else:
                    adjacent_list.append(lines[i][index-1])
                    adjacent_list.append(lines[i][index+1])

                    adjacent_list.append(lines[i-1][index-1])
                    adjacent_list.append(lines[i-1][index])
                    adjacent_list.append(lines[i-1][index+1])

                    adjacent_list.append(lines[i+1][index-1])
                    adjacent_list.append(lines[i+1][index])
                    adjacent_list.append(lines[i+1][index+1])

  
        for sym in symbols:
            if sym in adjacent_list:
               sum += int(match.group()) 
               break


print(sum)

#Kill me please took 4 hours 
        







