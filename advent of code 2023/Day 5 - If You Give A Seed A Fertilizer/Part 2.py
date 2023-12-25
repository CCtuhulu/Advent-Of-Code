import re

with open('Day 5 - If You Give A Seed A Fertilizer\input.txt', 'r') as file:
    lines = file.readlines()

#Setting lists for each step
while "\n" in lines:
    lines.remove("\n")

seeds = lines[1:lines.index("seed-to-soil map:\n")]
soils = lines[(lines.index("seed-to-soil map:\n")+1):lines.index("soil-to-fertilizer map:\n")]
fertilizers = lines[(lines.index("soil-to-fertilizer map:\n")+1):lines.index("fertilizer-to-water map:\n")]
waters = lines[(lines.index("fertilizer-to-water map:\n")+1):lines.index("water-to-light map:\n")]
lights = lines[(lines.index("water-to-light map:\n")+1):lines.index("light-to-temperature map:\n")]
temperatures = lines[(lines.index("light-to-temperature map:\n")+1):lines.index("temperature-to-humidity map:\n")]
humiditys = lines[(lines.index("temperature-to-humidity map:\n")+1):lines.index("humidity-to-location map:\n")]
locations = lines[(lines.index("humidity-to-location map:\n")+1):]


#----------------------- Setting up all lists ---------------------------------------------
seeds_prelist = [int(digit) for digit in re.findall(r'(\d+)',seeds[0])]

soil_line = []
for i,soil in enumerate(soils):
    soil_line.append([int(digit) for digit in re.findall(r'(\d+)', soil)])

fertilizer_line = []
for i,fertilizer in enumerate(fertilizers):
    fertilizer_line.append([int(digit) for digit in re.findall(r'(\d+)', fertilizer)])

water_line = []
for i,water in enumerate(waters):
    water_line.append([int(digit) for digit in re.findall(r'(\d+)', water)])

light_line = []
for i,light in enumerate(lights):
    light_line.append([int(digit) for digit in re.findall(r'(\d+)', light)])

temperature_line = []
for i,temperature in enumerate(temperatures):
    temperature_line.append([int(digit) for digit in re.findall(r'(\d+)', temperature)])

humidity_line = []
for i,humidity in enumerate(humiditys):
    humidity_line.append([int(digit) for digit in re.findall(r'(\d+)', humidity)])
    
location_line = []
for i,location in enumerate(locations):
    location_line.append([int(digit) for digit in re.findall(r'(\d+)', location)])

all_lines = {
    'soil': soil_line,
    'fertilizer': fertilizer_line,
    'water': water_line,
    'light': light_line,
    'temperature': temperature_line,
    'humidity': humidity_line,
    'location': location_line
}

# print(soil_line)
# print(fertilizer_line)
# print(water_line)
# print(light_line)
# print(temperature_line)
# print(humidity_line)
# print(location_line)
#-------------------------------------------------------------------------------------------
min = 999999999999

for i in range(0,len(seeds_prelist),2):
    for j in range(seeds_prelist[i+1]):

        current_nb = seeds_prelist[i]+j

        #seed to soil
        for soil in soil_line:
            if soil[1] <= current_nb <= (soil[1] + soil[2] - 1):
                current_nb = soil[0] + current_nb - soil[1]
                break
        
        #soil to fertilizer
        for fertilizer in fertilizer_line:
            if fertilizer[1] <= current_nb <= (fertilizer[1] + fertilizer[2] - 1):
                current_nb = fertilizer[0] + current_nb - fertilizer[1]
                break

        #fertilize to water
        for water in water_line:
            if water[1] <= current_nb <= (water[1] + water[2] - 1):
                current_nb = water[0] + current_nb - water[1]
                break

        #water to light
        for light in light_line:
            if light[1] <= current_nb <= (light[1] + light[2] - 1):
                current_nb = light[0] + current_nb - light[1]
                break

        #light to temperature
        for temperature in temperature_line:
            if temperature[1] <= current_nb <= (temperature[1] + temperature[2] - 1):
                current_nb = temperature[0] + current_nb - temperature[1]
                break

        #temperature to humidity
        for humidity in humidity_line:
            if int(humidity[1]) <= current_nb <= (int(humidity[1]) + int(humidity[2]) - 1):
                current_nb = int(humidity[0]) + (current_nb - int(humidity[1]))
                break

        #humidity to location
        for location in location_line:
            if location[1] <= current_nb <= (location[1] + location[2] - 1):
                current_nb = location[0] + current_nb - location[1]
                break

        if current_nb < min:
            min = current_nb
   

#TAKES 13 FOOKIN HOURS
print(min)
