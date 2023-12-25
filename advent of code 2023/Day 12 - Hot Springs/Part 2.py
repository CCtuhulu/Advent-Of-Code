# Got help
import functools

with open("Day 12 - Hot Springs\input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]



@functools.lru_cache(maxsize=None)
def calculate(spring, numbers):

    if spring == "":
        return 1 if numbers == () else 0
    
    if numbers == ():
        return 0 if "#" in spring else 1
    
    result = 0

    if spring[0] in ".?":
        result += calculate(spring[1:], numbers)

    if spring[0] in "?#":
        if numbers[0] <= len(spring) and "." not in spring[:numbers[0]] and (numbers[0] == len(spring) or spring[numbers[0]] != "#"):
            result += calculate(spring[numbers[0] + 1:], numbers[1:])


    return result


score = 0

for line in lines:
    spring, number = line.split()

    numbers = tuple(map(int,number.split(',')))

    spring = spring + "?" + spring + "?" + spring + "?" + spring + "?" + spring
    numbers *= 5

    score += calculate(spring, numbers)


print(score)