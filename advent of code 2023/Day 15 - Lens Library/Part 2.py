with open("Day 15 - Lens Library\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]


instructions = lines[0].split(',')
hashtable = {}

def hash(instruct):

    result = 0
    for chr in instruct:
        if chr in '-=':
            break
        result += ord(chr)
        result *= 17
        result %= 256
    return result

def action(instruct,key):

    if '-' in instruct:
        instr = instruct.replace('-','')
        if key in hashtable and len(hashtable[key]) > 0:
            
            if any(instr == tup[0] for tup in hashtable[key]):

                for index, tup in enumerate(hashtable[key]):
                    if instr == tup[0]:
                        hashtable[key].pop(index)

    elif '=' in instruct:
        instr = instruct.replace('=',' ')

        if key in hashtable:
            parts = instr.split()

            if any(parts[0] == tup[0] for tup in hashtable[key]):

                for index, tup in enumerate(hashtable[key]):
                    if parts[0] == tup[0]:
                        hashtable[key][index] = (parts[0],int(parts[1]))
            else:
                hashtable[key].append((parts[0],int(parts[1])))

        else:
            parts = instr.split()
            hashtable[key] = [(parts[0],int(parts[1]))]


for instruct in instructions:
    key = hash(instruct)
    action(instruct,key)


total = 0

for key in hashtable:

    for i,elem in enumerate(hashtable[key]):

        total += ( (key+1) * (i+1) * elem[1] )

print(total) 
