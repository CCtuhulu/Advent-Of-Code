import re

with open('Day 9 - Mirage Maintenance\input.txt', 'r') as file:
    lines = file.readlines()


datas = []
for line in lines:
    datas.append( [int(n) for n in re.findall((r'-?\d+'),line)] )


pyramid = []
values = []


for data in datas:

    pyramid.clear()
    pyramid.append(data)

    while pyramid[-1].count(0) != len(pyramid[-1]):
        temp_list = []

        for i in range(len(pyramid[-1])-1):
            diff = pyramid[-1][i+1] - pyramid[-1][i]
            temp_list.append(diff)

        pyramid.append(temp_list)
    pyramid[-1].append(0)
    for i in range(2, len(pyramid)+1):
        new_nb = pyramid[-i][-1] + pyramid[-i+1][-1]
        pyramid[-i].append(new_nb)

    values.append(pyramid[0][-1])


points = sum(values)

print(points)

