
lines = open('input.txt', 'r', encoding='utf8')

seeds = set()
locations = set()
seed2soil = set()
soil2fert = set()
fert2water = set()
water2light = set()
light2temp = set()
temp2humidity = set()
humidity2location = set()

active_set = None

for line in lines:
    line = line.strip()

    if line == '':
        continue

    if line[0:6] == 'seeds:':
        seeds_list = line.split(': ')[1].split()

        start_seed = None
        count = 0
        for entry in seeds_list:
            count += 1
            if count % 2 != 0:
                start_seed = entry
                continue

            seeds.add((int(start_seed), int(entry)))
        continue

    if line == 'seed-to-soil map:':
        active_set = seed2soil
        continue

    if line == 'soil-to-fertilizer map:':
        active_set = soil2fert
        continue

    if line == 'fertilizer-to-water map:':
        active_set = fert2water
        continue

    if line == 'water-to-light map:':
        active_set = water2light
        continue

    if line == 'light-to-temperature map:':
        active_set = light2temp
        continue

    if line == 'temperature-to-humidity map:':
        active_set = temp2humidity
        continue

    if line == 'humidity-to-location map:':
        active_set = humidity2location
        continue

    dst_start, src_start, map_range = line.split()

    active_set.add(
        (
            int(src_start),
            int(src_start) + int(map_range) + 1,
            int(dst_start) - int(src_start)
        )
    )

for start_and_range in seeds:
    start_seed = start_and_range[0]
    end_seed = start_seed + start_and_range[1] + 1

    for seed in range(start_seed, end_seed):

        soil = seed
        for seedmap in seed2soil:
            if seed in range(seedmap[0], seedmap[1]):
                soil = seed + seedmap[2]
                break

        fert = soil
        for soilmap in soil2fert:
            if soil in range(soilmap[0], soilmap[1]):
                fert = soil + soilmap[2]
                break

        water = fert
        for fertmap in fert2water:
            if fert in range(fertmap[0], fertmap[1]):
                water = fert + fertmap[2]
                break

        light = water
        for watermap in water2light:
            if water in range(watermap[0], watermap[1]):
                light = water + watermap[2]
                break

        temp = light
        for lightmap in light2temp:
            if light in range(lightmap[0], lightmap[1]):
                temp = light + lightmap[2]
                break

        humidity = temp
        for tempmap in temp2humidity:
            if temp in range(tempmap[0], tempmap[1]):
                humidity = temp + tempmap[2]
                break

        location = humidity
        for humiditymap in humidity2location:
            if humidity in range(humiditymap[0], humiditymap[1]):
                location = humidity + humiditymap[2]
                break

        locations.add(location)

print(f'The lowest possible location number is: {min(locations)}')
print('')