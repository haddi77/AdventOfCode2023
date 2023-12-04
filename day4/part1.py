
lines = open('input.txt', 'r', encoding='utf8')

points_sum = 0

while lines:
    line = lines.readline().strip()
    if line == '':
        break

    winning_nos, drawn_nos = line.split(': ')[1].split(' | ')

    winning_nos = set(winning_nos.split())
    drawn_nos = set(drawn_nos.split())
    won_nos = drawn_nos.intersection(winning_nos)
    points_sum += int(2 ** (len(won_nos) - 1))

print(points_sum)