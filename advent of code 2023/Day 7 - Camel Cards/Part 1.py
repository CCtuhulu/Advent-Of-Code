import re

with open('Day 7 - Camel Cards\input.txt', 'r') as file:
    lines = file.readlines()

ranking = []

for line in lines:

    hand, bid = line.split(' ')
    bid = int(bid)
    hand = list(hand)
    for h in hand:
        if h.isdigit():
            hand[hand.index(h)] = int(h)
        
        elif h == "T":
            hand[hand.index(h)] = 10
        
        elif h == "J":
            hand[hand.index(h)] = 11

        elif h == "Q":
            hand[hand.index(h)] = 12

        elif h == "K":
            hand[hand.index(h)] = 13

        elif h == "A":
            hand[hand.index(h)] = 14


    ranking.append((hand,bid))



for i in range(len(ranking)):

    for j in range(1,len(ranking)-i):
        
        hand1_result = []
        hand2_result = []


        for k in range(2,15):
            if ranking[i][0].count(k):
                hand1_result.append(ranking[i][0].count(k))

            if ranking[i+j][0].count(k):
                hand2_result.append(ranking[i+j][0].count(k))  

        hand1_result.sort(reverse = True)
        hand2_result.sort(reverse = True)

        if hand2_result < hand1_result:
            temp = ranking[i+j]
            ranking[i+j] = ranking[i]
            ranking[i] = temp

        elif hand2_result > hand1_result:
            pass
        
        else:
            if ranking[i+j] < ranking[i]:
                temp = ranking[i+j]
                ranking[i+j] = ranking[i]
                ranking[i] = temp

points = 0

for i in range(len(ranking)):
    points += (i+1) * ranking[i][1]


print(points)
