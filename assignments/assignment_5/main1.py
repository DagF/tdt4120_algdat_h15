from sys import stdin

Inf = float(1e3000)
False = 0
True = 1


def mst(nm):
    node_count = len(nm)
    nodes = [0]
    max_edge = 0

    while len(nodes) < node_count:
        edges = []
        for node in nodes:
            edges.extend(nm[node])

        small_edge = edges[0]

        for edge in edges:
            if edge[0][1] not in nodes:
                if edge[1] < small_edge[1]:
                    small_edge = edge

        n = small_edge[0][1]
        nodes.append(n)
        if small_edge[1] > max_edge:
            max_edge = small_edge[1]

    return max_edge

def main():
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = []
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node].append(((node, nabo), vekt))
        node += 1
    print mst(nabomatrise)

main()