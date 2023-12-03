from string import punctuation

symbols = set(punctuation)
symbols.remove('.')

lines = open('input.txt', 'r', encoding='utf8')

part_no_sum = 0

line_prev = ''
line_cur = lines.readline().strip()
line_next = lines.readline().strip()

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

            if line_next:
                neighbours_bottom = line_next[other_lines_start_at: other_lines_end_at + 1]

            if num_start_idx > 0:
                neighbour_left = line_cur[num_start_idx - 1]

            if num_end_idx < len(line_cur) - 1:
                neighbour_right = line_cur[num_end_idx + 1]


            neighbours = set(neighbour_left + neighbour_right + neighbours_top + neighbours_bottom)

            nearby_parts = neighbours.intersection(symbols)
            if len(nearby_parts) > 0:
                print(f'{num} is the part number for {nearby_parts}')
                part_no_sum += int(num)

            else:
                print(f'{num} is not a part number')

            num = None
            num_start_idx = None
            num_end_idx = None
    line_prev = line_cur
    line_cur = line_next
    if line_cur == '':
        break

    line_next = lines.readline().strip()

print(f'The sum of all part numbers is {part_no_sum}')