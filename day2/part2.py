from functools import reduce
from copy import copy

lines = open('input.txt', 'r', encoding='utf8')

zero_bag = {
    'red': 0,
    'green': 0,
    'blue': 0
}

sum = 0

while lines:
    line = lines.readline().strip()
    if line == '':
        break

    game_id = int(line.split(': ')[0].replace('Game ', ''))
    rounds_text = line.split(': ')[1].split('; ')
    min_bag = copy(zero_bag)
    for round_text in rounds_text:
        for color in round_text.split(', '):
            for bag_color_name, bag_color_amount in min_bag.items():
                if bag_color_name in color:
                    color_amount = int(color.replace(bag_color_name, '').strip())
                    if color_amount > bag_color_amount:
                        min_bag[bag_color_name] = color_amount
                    break
    # print(min_bag)
    round_min_bag_product = reduce(lambda x, y: x * y, min_bag.values())
    # print(round_min_bag_product)
    sum += round_min_bag_product

print(sum)