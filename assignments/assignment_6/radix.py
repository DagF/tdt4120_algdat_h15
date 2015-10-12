from sys import stdin

def sorter(list):
    buckets = {}
    m = 10

    done = False

    while not done:
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        done = True
        for element in list:
            digit = (element % m) // (m / 10)
            buckets[digit].append(element)
            if digit != 0:
                done = False
        m *= 10
        list = []

        extend = list.extend
        for bucket in buckets:
            extend(bucket)
    return list


def memorize(f):
    memo = {}
    def helper(l,x):
        if x not in memo:
            memo[x] = f(l,x)
        return memo[x]
    return helper

@memorize
def search(list, lim):
    list_length = len(list)

    first = 0
    last = list_length - 1


    while True:
        midpoint = (first + last) // 2
        if lim < list[midpoint]:
            if midpoint > 0:
                if lim > list[midpoint-1]:
                    return [list[midpoint-1], list[midpoint]]
            elif midpoint == 0:
                return [list[midpoint], list[midpoint]]

            last = midpoint - 1


        elif lim > list[midpoint]:
            if midpoint < list_length -2:
                if lim < list[midpoint+1]:
                    return [list[midpoint], list[midpoint+1]]
            elif midpoint == list_length - 1:
                return [list[midpoint], list[midpoint]]

            first = midpoint + 1

        else:
            return [lim,lim]








def finn(list, nedre, ovre):
    return [search(list, nedre)[0], search(list,ovre)[1]]


def main():
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x))


    sortert = sorter(liste)
    ans = []
    append = ans.append
    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        append( str(resultat[0]) + " " + str(resultat[1]))
    print("\n".join(ans))

main()