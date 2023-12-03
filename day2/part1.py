
lines = open('input.txt', 'r', encoding='utf8')

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

while lines:
    line = lines.readline().strip()
    if line == '':
        break

    game_id = int(line.split(': ')[0].replace('Game ', ''))
    rounds_text = line.split(': ')[1].split('; ')

    for round_text in rounds_text:
        for color in round_text.split(', '):
            for bag_color_name, bag_color_amount in bag.items():
                if bag_color_name in color:
                    color_amount = int(color.replace(bag_color_name, '').strip())
                    if color_amount > bag_color_amount:
                        break
            else:
                continue

            break

        else:
            continue

        break

    else:
        sum += game_id

print(sum)