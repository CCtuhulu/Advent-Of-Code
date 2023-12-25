import re


with open("Day 7 - Some Assembly Required\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

operations = ['AND', 'RSHIFT', 'LSHIFT', 'NOT', 'OR']

tasks = []

for line in lines:

    part = line.split('-> ')
    
    task = []

    gotop = False
    for op in operations:
        if op in part[0]:
            task.append(op)
            part[0] = part[0].replace(op,'')
            gotop = True
            break

    if not gotop:
        task.append('ASSIGN')
    
    words = re.findall(r'\b\w+\b', part[0])
    task.append(words[0])
    if len(words) == 2:
        task.append(words[1])

    task.append(part[1])

    tasks.append(task)

found_a = False

values = {}
while not found_a:

    for task in tasks:
        #ASSIGN TASK
        if task[0] == 'ASSIGN' and (task[1] in values or task[1].isdigit()):
            if task[1].isdigit():
                values[task[2]] = int(task[1])
            else:
                values[task[2]] = values[task[1]]

            tasks.remove(task)

        #NOT TASK
        elif task[0] == 'NOT' and task[1] in values:
            values[task[2]] = values[task[1]] ^ 0xFFFF
            tasks.remove(task)

        elif task[0] == 'AND' and task[2] in values and (task[1] in values or task[1].isdigit()):

            if task[1].isdigit():
                values[task[3]] = values[task[2]] & int(task[1])
            else:
                values[task[3]] = values[task[2]] & values[task[1]]
            tasks.remove(task)

        elif task[0] == 'OR' and task[1] in values and task[2] in values:
            values[task[3]] = values[task[1]] | values[task[2]]
            tasks.remove(task)

        elif task[0] == 'LSHIFT' and task[1] in values:
            values[task[3]] = values[task[1]] << int(task[2])
            tasks.remove(task)

        elif task[0] == 'RSHIFT' and task[1] in values:
            values[task[3]] = values[task[1]] >> int(task[2])
            tasks.remove(task)

    if 'a' in values:
        found_a = True

print(values['a'])
                 
