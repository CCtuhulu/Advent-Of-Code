import re

with open('Day 4 - Scratchcards\input.txt', 'r') as file:
    lines = file.readlines()

final_list = []

for i,line in enumerate(lines):
    final_list.append((i+1, line, 1))


parts = []

points = 0


for i,mem in enumerate(final_list):

    parts.clear()

    #split the line into card and numbers_got
    parts = final_list[i][1].split("|")
    card_numbers = re.findall(r'(\d+)', parts[0])
    player_numbers = re.findall(r'(\d+)', parts[1])

    #remove line number
    card_numbers.pop(0)

    winnings = 0

    for cn in card_numbers:
            if cn in player_numbers:
                winnings += 1

            while cn in player_numbers:
                player_numbers.remove(cn)

    for j in range(winnings):
        new_appearance = final_list[int(i+j+1)][2] + final_list[int(i)][2]
        final_list[int(i+j+1)] = (final_list[int(i+j+1)][0], final_list[int(i+j+1)][1], new_appearance)

    points += final_list[i][2]




print(points)