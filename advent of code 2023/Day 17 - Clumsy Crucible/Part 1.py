#Tooo slow without heapq
import heapq

with open("Day 17 - Clumsy Crucible\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

LEFT = 0
RIGHT = 1


graph = {}
#Creating the adjacency list
for i,line in enumerate(lines):

    for j in range(len(lines[0])):

        coord = (j,i)
        graph[coord] = {}
        if j > 0:
            neighor_coord = (j-1,i)
            graph[coord][neighor_coord] = int(lines[neighor_coord[1]][neighor_coord[0]])

        if j < len(lines[0])-1:
            neighor_coord = (j+1,i)
            graph[coord][neighor_coord] = int(lines[neighor_coord[1]][neighor_coord[0]])

        if i > 0:
            neighor_coord = (j,i-1)
            graph[coord][neighor_coord] = int(lines[neighor_coord[1]][neighor_coord[0]])

        if i < len(lines)-1:
            neighor_coord = (j,i+1)
            graph[coord][neighor_coord] = int(lines[neighor_coord[1]][neighor_coord[0]])


def dijkstra(graph, start):

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    end = (len(lines)-1,len(lines[0])-1)

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))


    return distances[end]


print(dijkstra(graph,(0,0)))