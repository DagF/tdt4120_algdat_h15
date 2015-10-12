from sys import stdin
from itertools import repeat

def merge(decks):
    ind = 0
    d_l = len(decks)-1

    while ind < d_l:
        d_1 = decks[ind]
        d_2 = decks[ind + 1]
        i,j,k = 0,0,0
        d1l = len(d_1)
        d2l = len(d_2)
        tmp = [None] * (d1l+d2l)
        while i < d1l and j < d2l:
            if d_1[i][0] < d_2[j][0]:
                tmp[k] = d_1[i]
                i += 1
            else:
                tmp[k] = d_2[j]
                j += 1
            k += 1

        while i < d1l:
            tmp[k] = d_1[i]
            i += 1
            k += 1

        while j < d2l:
            tmp[k] = d_2[j]
            j += 1
            k += 1

        ind += 1
        decks[ind] = tmp

    mre = ""
    for dex in decks[d_l]:
        mre += dex[1]

    return mre

dec = []
d_a = dec.append
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    d_a(deck)
print merge(dec)