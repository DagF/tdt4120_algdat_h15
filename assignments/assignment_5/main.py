from sys import stdin

Inf = float(1e3000)
False = 0
True = 1


def mst(edges, node_count):
    edges = sorted(edges, key=lambda tup: tup[2])
    nodes = [0]
    for edge in edges:
        print(edge[0],edge[1],edge[2])

    return None

def main():
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    node = 0
    edges = []
    for linje in linjer:
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            edges.append((node,nabo,vekt))
        node += 1
    print mst(edges, node)

main()
