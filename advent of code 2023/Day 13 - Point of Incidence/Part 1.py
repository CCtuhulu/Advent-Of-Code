with open("Day 13 - Point of Incidence\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


def reflection(valley):

    length = len(valley[0])
    height = len(valley)


    #Check horizental symetry
    for i in range(0,height-1):
        reflect = True
        offset = 0
        while reflect:
            if (i - offset < 0) or (i + 1 + offset > height-1):
                break

            for j in range(0,offset+1):
                if(valley[i-j] != valley[i+j+1]):
                    reflect = False
                    break
                
            offset += 1
        
        if reflect:
            return (i+1)*100
        
    #Check Vertical symetry
    for i in range(0,length-1):
        reflect = True
        offset = 0

        while reflect:
            if (i - offset < 0) or (i + 1 + offset > length-1):
                break

            for j in range(0,offset+1):
                for k in range(0,height):
                    if(valley[k][i-j] != valley[k][i+j+1]):
                        reflect = False
                        break
                
            offset += 1
        
        if reflect:
                return i+1
    

score = 0
valley = []
for i,line in enumerate(lines):


    if i == (len(lines)-1):
        valley.append(line)

    if line == "" or i == (len(lines)-1):
        score += reflection(valley)
        valley.clear()
    
    else:
        valley.append(line)



print(score)