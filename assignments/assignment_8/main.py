from sys import stdin, stderr

def beste_sti(nm, sans):
    if sans[0] == 0.0:
        return 0
    visited = {}
    discovered = [0]
    previous = {}
    last_node =len(nm) -1

    while visited.get(last_node) == None or len(discovered) != 0:

        max_sansynlighet = 0
        max_sansynlighet_node = None
        for node in discovered:
            if sans[node] > max_sansynlighet:
                max_sansynlighet = sans[node]
                max_sansynlighet_node = node



        if previous.get(max_sansynlighet_node):
            visited[max_sansynlighet_node] = previous[max_sansynlighet_node] * max_sansynlighet
        else:
            visited[max_sansynlighet_node] = max_sansynlighet

        new_dic = []
        discovered.remove(max_sansynlighet_node)
        for n in nm[max_sansynlighet_node]:

            if not visited.get(n) and n not in discovered:

                new_dic.append(n)
                previous[n] = max_sansynlighet_node

        discovered.extend(new_dic)

    out = []
    n = len(nm) - 1
    while n != 0:
        out.append(str(n))
        n = previous[n]

    out.append("0")
    out.reverse()
    print(visited)
    return "-".join(out)




n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naboer = [int(nabo) for nabo in linje.split()]
    nabomatrise.append(naboer)

print beste_sti(nabomatrise, sannsynligheter)