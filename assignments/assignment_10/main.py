from sys import stdin, maxint

Inf = maxint

def korteste_rute(rekkefolge, nabomatrise, byer):
    r = len(rekkefolge)
    if r == 1:
        return 0
    i, j = 0, 1
    sum = 0
    while i < r:
        s = dijkstra(byer, nabomatrise, rekkefolge[i], rekkefolge[j])
        #print("from: ", rekkefolge[i], ", to: ", rekkefolge[j])
        if s == -1:
            return "umulig"

        sum += s
        i += 1
        j += 1
        if j == r:
            j = 0

    return sum


def dijkstra(byer, nabomatrise, start, slutt):
    kostnad = [Inf] * byer
    oppdaget = [(start, 0, None)]
    parent = [None]* byer
    parent[start] = start
    besokt = []

    while len(oppdaget) and slutt not in besokt:
        #print("besokt", besokt)
        #print("oppdaget", oppdaget)

        min = (None,maxint, None)
        for node in oppdaget:
            if node[1] < min[1]:
                min = node

        min_by = min[0]
        kostnad[min_by] = min[1]
        parent[min_by] = min[2]
        #print("min by: ", min_by)
        #print("kost: ",kostnad)
        #print("parent: ",parent)

        for op in oppdaget:
            if op[0] == min_by:
                oppdaget.remove(op)
        besokt.append(min_by)

        for by in range(byer):
            kos = nabomatrise[min_by][by]
            #print("kos: ", kos)
            if kos > -1:
                kos += kostnad[min_by]
                #print("kos2 :", kos)
                #if kostnad[by] < kos:
                #    kostnad[by] = kos
                #    parent[by] = min_by

                if by not in besokt and by not in oppdaget:
                    oppdaget.append((by,kos,kostnad[min_by]))





    if kostnad[slutt] == maxint:
        return -1
    #print(kostnad)
    return kostnad[slutt]

testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = [int(by) for by in stdin.readline().split()]
    nabomatrise = []
    for by in range(byer):
        nabomatrise.append([int(kos) for kos in stdin.readline().split()])

    print korteste_rute(rekkefolge,  nabomatrise, byer)