with open("Day 13 - Point of Incidence\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


def reflection(valley,part1score):

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
                if(valley[i-j] != valley[i+j+1]) and part1score != (i+1)*100:
                    reflect = False
                    break
                
            offset += 1
        
        if reflect and part1score != (i+1)*100:
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
                    if(valley[k][i-j] != valley[k][i+j+1]) and (i+1)!=part1score:
                        reflect = False
                        break
                
            offset += 1
        
        if reflect and part1score != (i+1):
                return i+1
        
    return 0
    

def bruteforcecauselazy(valley):
    part1score = reflection(valley,-1)
    length = len(valley[0])
    height = len(valley)

    for j in range(height):
        for i in range(length):
            new_valley = [list(string) for string in valley]
            if new_valley[j][i] == '.':
                new_valley[j][i] = '#'
            else:
                new_valley[j][i] = '.'

            new_ref = reflection(new_valley,part1score) 

            if new_ref != part1score and new_ref > 0:
                return new_ref  
            
    return 0  


            

score = 0
valley = []
for i,line in enumerate(lines):


    if i == (len(lines)-1):
        valley.append(line)

    if line == "" or i == (len(lines)-1):
        score += bruteforcecauselazy(valley)
        valley.clear()
    
    else:
        valley.append(line)



print(score)