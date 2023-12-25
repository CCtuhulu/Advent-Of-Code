import re

with open('Day 4 - Scratchcards\input.txt', 'r') as file:
    lines = file.readlines()


parts = []
points = 0

for i,line in enumerate(lines):
    
    parts.clear()
    
    #split the line into card and numbers_got
    parts = line.split("|")

    card_numbers = re.findall(r'(\d+)', parts[0])
    player_numbers = re.findall(r'(\d+)', parts[1])

    #remove the first number in card_numbers because it is the card number
    card_numbers.pop(0)

    winnings = 0
    for cn in card_numbers:


        if cn in player_numbers:
            winnings += 1
            
            while cn in player_numbers:
                player_numbers.remove(cn)


    if winnings == 0:
        pass
    else:
        points += (2**(winnings-1))


print(points)