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
    oppdaget = [(start, 0)]
    o_a = oppdaget.append
    besokt = []
    b_a = besokt.append
    o_r = oppdaget.remove

    while len(oppdaget) and slutt not in besokt:

        min = (None,maxint)
        for node in oppdaget:
            if node[1] < min[1]:
                min = node

        min_by = min[0]
        kostnad[min_by] = min[1]

        for op in oppdaget:
            if op[0] == min_by:
                o_r(op)
        b_a(min_by)

        for by in range(byer):
            kos = nabomatrise[min_by][by]
            if kos > -1:
                kos += kostnad[min_by]

                if by not in besokt and by not in oppdaget:
                    o_a((by,kos))

    if kostnad[slutt] == maxint:
        return -1
    return kostnad[slutt]


def main():
    out = []
    append = out.append
    testcases = int(stdin.readline())
    for test in range(testcases):
        byer = int(stdin.readline())
        rekkefolge = [int(by) for by in stdin.readline().split()]
        nabomatrise = []
        n_a = nabomatrise.append
        for by in range(byer):
            n_a([int(kos) for kos in stdin.readline().split()])

        append(str(korteste_rute(rekkefolge,  nabomatrise, byer)) )
    print("\n".join(out))

main()