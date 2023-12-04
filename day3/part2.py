from string import punctuation

gear = '*'

lines = open('input.txt', 'r', encoding='utf8')

part_no_sum = 0

line_prev = ''
line_cur = lines.readline().strip()
line_next = lines.readline().strip()
line_no = 0

gears = {}

while lines:
    num = None
    num_start_idx = None
    num_end_idx = None
    for idx, letter in enumerate(line_cur):
        if letter.isdigit():
            if not num:
                num_start_idx = idx
                num = letter

            else:
                num += letter

        if num and not letter.isdigit() or num and idx == len(line_cur) - 1:
            num_end_idx = idx - 1
            if idx == len(line_cur) - 1:
                num_end_idx = idx

            neighbours_top = ''
            neighbours_bottom = ''
            neighbour_left = ''
            neighbour_right = ''

            other_lines_start_at = max(0, num_start_idx - 1)
            other_lines_end_at = min(len(line_cur) - 1, num_end_idx + 1)

            if line_prev:
                neighbours_top = line_prev[other_lines_start_at: other_lines_end_at + 1]
                if gear in neighbours_top:
                    gear_address = f'{line_no - 1},{neighbours_top.index(gear) + other_lines_start_at}'
                    if gear_address not in gears:
                        gears[gear_address] = [int(num)]

                    else:
                        gears[gear_address] += [int(num)]

            if line_next:
                neighbours_bottom = line_next[other_lines_start_at: other_lines_end_at + 1]
                if gear in neighbours_bottom:
                    # new_gears = {f'{line_no + 1},{neighbours_bottom.index(gear) + other_lines_start_at}': num}
                    # gears.update(new_gears)
                    gear_address = f'{line_no + 1},{neighbours_bottom.index(gear) + other_lines_start_at}'
                    if gear_address not in gears:
                        gears[gear_address] = [int(num)]

                    else:
                        gears[gear_address] += [int(num)]

            if num_start_idx > 0:
                neighbour_left = line_cur[num_start_idx - 1]
                if neighbour_left == gear:
                    gear_address = f'{line_no},{num_start_idx - 1}'
                    if gear_address not in gears:
                        gears[gear_address] = [int(num)]

                    else:
                        gears[gear_address] += [int(num)]

            if num_end_idx < len(line_cur) - 1:
                neighbour_right = line_cur[num_end_idx + 1]
                if neighbour_right == gear:
                    gear_address = f'{line_no},{num_end_idx + 1}'
                    if gear_address not in gears:
                        gears[gear_address] = [int(num)]

                    else:
                        gears[gear_address] += [int(num)]

            num = None
            num_start_idx = None
            num_end_idx = None
    line_prev = line_cur
    line_cur = line_next
    if line_cur == '':
        break

    line_next = lines.readline().strip()
    line_no += 1

for gear, gear_nos in gears.items():
    if len(gear_nos) > 1:
        part_no_sum += gear_nos[0] * gear_nos[1]

print(part_no_sum)