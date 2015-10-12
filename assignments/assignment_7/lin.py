from sys import stdin
from itertools import repeat

def merge(decks):
    d_l = 0

    for deck in decks:
        max_card = 0
        for c in deck:
            if c[0] > max_card:
                max_card = c[0]
        d_l += max_card

    n_d = [None] * d_l

    for deck in decks:
        for card in deck:
            n_d[card[0]-1] = card

    ret = ""
    for n in n_d:
        if n is not None:
            ret += n[1]

    return ret

dec = []
d_a = dec.append
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    d_a(deck)
print merge(dec)