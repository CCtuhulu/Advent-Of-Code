import hashlib

with open('Day 4 - The Ideal Stocking Stuffer\input.txt', 'r') as file:
    lines = file.readlines()

i = 0
while True:
    input = (lines[0]+str(i)).encode('utf-8')
    hashed = hashlib.md5(input).hexdigest()
    
    if hashed[0] == hashed[1] == hashed[2] == hashed [3] == hashed[4] == hashed[5] == '0':
        break

    i += 1

print(i)