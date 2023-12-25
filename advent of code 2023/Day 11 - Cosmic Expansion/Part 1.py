
with open("Day 11 - Cosmic Expansion\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


#Check all lines that are empty and galaxies coords
vertical_empty = []
horizental_empty = []
galaxies = []
vertical = [1] * len(lines[0])

for i, line in enumerate(lines):
    horiz_empty = True
    for j, chr in enumerate(line):
        if chr != '.':
            horiz_empty = False
            vertical[j] = 0
            galaxies.append((j,i))

    if horiz_empty:
        horizental_empty.append(i)

for i,v in enumerate(vertical):
    if v:
        vertical_empty.append(i)

#Count the distances

total_distances = 0

for i, galaxy in enumerate(galaxies):
    
    for other_galaxy in galaxies[i+1:]:
        multiple_horiz = [x for x in horizental_empty if min(other_galaxy[1],galaxy[1]) < x < max(other_galaxy[1],galaxy[1])]
        multiple_vertic = [x for x in vertical_empty if min(other_galaxy[0],galaxy[0]) < x < max(other_galaxy[0],galaxy[0])]
        distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1]) + len(multiple_horiz) + len(multiple_vertic)
        total_distances += distance

print(total_distances)
