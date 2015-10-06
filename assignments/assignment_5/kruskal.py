from sys import stdin

Inf = float(1e3000)



def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]

def union(C, R, u, v):
    u,v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v],u,v) for u in range(len(G)) for v in G[u]]
    T = set()
    C,R = {u:u for u in G}, {u:0 for u in G}
    for w, u, v in sorted(E):
        if find(C, u) != find(C,v):
            T.add((w,u,v))
            union(C, R, u, v)

    max = 0
    for edge in T:
        if T[0] > max:
            max = T[0]

    return max

def main():
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print (kruskal(nabomatrise))

main()