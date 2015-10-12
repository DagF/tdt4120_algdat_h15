from sys import stdin
from itertools import repeat

def merge_l(lef, rig):
    l_h = lef
    r_h = rig
    d_l = len(r_h) + len(l_h)
    list = [None] * d_l

    i,j,k = 0,0,0
    left_length = len(l_h)
    right_length = len(r_h)

    while i < left_length and j < right_length:
        if l_h[i] < r_h[j]:
            list[k] = l_h[i]
            i += 1
        else:
            list[k] = r_h[j]
            j += 1
        k += 1

    while i < left_length:
        list[k] = l_h[i]
        i += 1
        k += 1

    while j < right_length:
        list[k] = r_h[j]
        j += 1
        k += 1

    return list

def merge(decks):
    l_d = len(decks)
    if l_d > 2:
        mid = l_d // 2
        return merge_l(
            merge(decks[:mid]),
            merge(decks[mid:])
        )
    elif l_d == 2:
        return merge_l(decks[0], decks[1])
    else:
        return decks[0]

def main():
    dec = []
    d_a = dec.append
    ret = []
    r_a = ret.append
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        d_a(deck)

    mer = merge(dec)
    r = ""
    for m in mer:
        r += m[1]
    r_a(r)
    print("\n".join(ret))

main()