
lines = open('input.txt', 'r', encoding='utf8')

cards = {}

cards_sum = 0

points_sum = 0

while lines:
    line = lines.readline().strip()
    if line == '':
        break

    card_no, numbers = line.split(': ')
    card_no = int(card_no.replace('Card ', ''))
    if card_no in cards.keys():
        cards[card_no] += 1
    else:
        cards[card_no] = 1

    cards_sum += cards[card_no]

    winning_nos, drawn_nos = numbers.split(' | ')

    winning_nos = set(winning_nos.split())
    drawn_nos = set(drawn_nos.split())
    won_nos = drawn_nos.intersection(winning_nos)
    how_many_cards = len(won_nos)
    multiplier = cards[card_no]

    for count_cards in range(1, how_many_cards + 1):
        if card_no + count_cards in cards.keys():
            cards[card_no + count_cards] += multiplier
        else:
            cards[card_no + count_cards] = multiplier


print(cards_sum)