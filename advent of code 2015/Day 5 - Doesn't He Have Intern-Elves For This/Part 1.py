with open("Day 5 - Doesn't He Have Intern-Elves For This\input.txt", 'r') as file:
    lines = file.readlines()

voyels = ['a', 'e', 'i', 'o', 'u']
nono_words = ['ab', 'cd', 'pq', 'xy']


nice_word = 0

for line in lines:
    nice = True

    for n in nono_words:
        if n in line:
            nice = False
            break
    
    if nice:

        nice1 = False 
        v_counter = 0
        for v in voyels:
            v_counter += line.count(v)

            if v_counter >= 3:
                nice1 = True
                break

        if nice1:

            for i in range(len(line)-1):
                if line[i] == line[i+1]:
                    nice_word += 1
                    break


print(nice_word)