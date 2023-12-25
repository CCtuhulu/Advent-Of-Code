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


seeds_list = re.findall(r'(\d+)',seeds[0])

end_list = []

for seed in seeds_list:

    current_nb = int(seed)

    #seed to soil
    soil_line = []
    for soil in soils:
        soil_line.clear()
        soil_line = re.findall(r'(\d+)',soil)
        if int(soil_line[1]) <= current_nb <= (int(soil_line[1]) + int(soil_line[2]) - 1):
            current_nb = int(soil_line[0]) + (current_nb - int(soil_line[1]))
            break
    
    #soil to fertilizer
    fertilizer_line = []
    for fertilizer in fertilizers:
        fertilizer_line.clear()
        fertilizer_line = re.findall(r'(\d+)',fertilizer)
        if int(fertilizer_line[1]) <= current_nb <= (int(fertilizer_line[1]) + int(fertilizer_line[2]) - 1):
            current_nb = int(fertilizer_line[0]) + (current_nb - int(fertilizer_line[1]))
            break

    #fertilize to water
    water_line = []
    for water in waters:
        water_line.clear()
        water_line = re.findall(r'(\d+)',water)
        if int(water_line[1]) <= current_nb <= (int(water_line[1]) + int(water_line[2]) - 1):
            current_nb = int(water_line[0]) + (current_nb - int(water_line[1]))
            break

    #water to light
    light_line = []
    for light in lights:
        light_line.clear()
        light_line = re.findall(r'(\d+)',light)
        if int(light_line[1]) <= current_nb <= (int(light_line[1]) + int(light_line[2]) - 1):
            current_nb = int(light_line[0]) + (current_nb - int(light_line[1]))
            break

    #light to temperature
    temperature_line = []
    for temperature in temperatures:
        temperature_line.clear()
        temperature_line = re.findall(r'(\d+)',temperature)
        if int(temperature_line[1]) <= current_nb <= (int(temperature_line[1]) + int(temperature_line[2]) - 1):
            current_nb = int(temperature_line[0]) + (current_nb - int(temperature_line[1]))
            break

    #temperature to humidity
    humidity_line = []
    for humidity in humiditys:
        humidity_line.clear()
        humidity_line = re.findall(r'(\d+)',humidity)
        if int(humidity_line[1]) <= current_nb <= (int(humidity_line[1]) + int(humidity_line[2]) - 1):
            current_nb = int(humidity_line[0]) + (current_nb - int(humidity_line[1]))
            break

    #humidity to location
    location_line = []
    for location in locations:
        location_line.clear()
        location_line = re.findall(r'(\d+)',location)
        if int(location_line[1]) <= current_nb <= (int(location_line[1]) + int(location_line[2]) - 1):
            current_nb = int(location_line[0]) + (current_nb - int(location_line[1]))
            break

    end_list.append(current_nb)

print(min(end_list))