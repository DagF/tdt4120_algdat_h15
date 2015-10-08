from sys import stdin

def sorter(list):
    list_length = len(list)
    if list_length > 1:
        midpoint = list_length // 2
        left_half = list[:midpoint]
        right_half = list[midpoint:]

        sorter(left_half)
        sorter(right_half)

        i,j,k = 0,0,0
        left_length = len(left_half)
        right_length = len(right_half)

        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            list[k] = right_half[j]
            j += 1
            k += 1


    return list

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

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)

        print( str(resultat[0]) + " " + str(resultat[1]))

main()