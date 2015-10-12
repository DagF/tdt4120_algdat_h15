from sys import stdin
from itertools import repeat

def merge(decks):
    d_i = []
    d_n = []
    d_l = []
    __l = len(decks)

    mer = ""
    dia = d_i.append
    dna = d_n.append
    dla = d_l.append
    for i in range(0, __l):
        dia(0)
        dna(True)
        dla(len(decks[i]))

    while True in d_n:
        min = None
        m_i = None
        for i in xrange(0,__l):
            if min == None or (d_n[i] == True and decks[i][d_i[i]][0] < min):
                if d_n[i] == True:
                    min = decks[i][d_i[i]][0]
                    m_i = i

        mer += decks[m_i][d_i[m_i]][1]
        d_i[m_i] += 1
        if d_l[m_i] == d_i[m_i]:
            d_n[m_i] = False

    return mer

dec = []
d_a = dec.append
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    d_a(deck)
print merge(dec)