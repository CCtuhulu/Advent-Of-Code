with open("Day 5 - Doesn't He Have Intern-Elves For This\input.txt", 'r') as file:
    lines = file.readlines()


nice_word = 0

for line in lines:
    
    nice = False
    line = line.replace('\n','')

    for i in range(len(line)-1):
        test = line
        pair = line[i] + line[i+1]
        test = test.replace(pair, ')(', 1)
        if pair in test:
            nice = True
            break
    
    nice1 = False

    if nice:

        for i in range(len(line)-2):

            if line[i] == line[i+2]:
                nice1 = True
                break

    if nice1:
        nice_word += 1

print(nice_word)