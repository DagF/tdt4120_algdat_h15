from sys import stdin

def sor(arr):
    les, equ, gre = [], [], []
    l_a, g_a, e_a = les.append, gre.append, equ.append

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                l_a(x)
            if x == pivot:
                e_a(x)
            if x > pivot:
                g_a(x)
        return sor(les)+equ+sor(gre)
    else:
        return arr


def mem(f):
    memo = {}
    def hel(l,x):
        if x not in memo:
            memo[x] = f(l,x)
        return memo[x]
    return hel

@mem
def sea(lis, lim):
    l_l = len(lis)

    fir = 0
    las = l_l - 1


    while 1:
        mid = (fir + las) // 2
        if lim < lis[mid]:
            if mid > 0:
                if lim > lis[mid-1]:
                    return [lis[mid-1], lis[mid]]
            elif mid == 0:
                return [lis[mid], lis[mid]]

            las = mid - 1


        elif lim > lis[mid]:
            if mid < l_l -2:
                if lim < lis[mid+1]:
                    return [lis[mid], lis[mid+1]]
            elif mid == l_l - 1:
                return [lis[mid], lis[mid]]

            fir = mid + 1

        else:
            return [lim,lim]





def finn(lis, ned, ovr):
    return [sea(lis, ned)[0], sea(lis,ovr)[1]]


def main():
    lis = []
    l_a = lis.append
    for x in stdin.readline().split():
        l_a(int(x))

    sot = sor(lis)
    ans = []
    app = ans.append

    for linje in stdin:
        ord = linje.split()
        min = int(ord[0])
        mak = int(ord[1])
        res = finn(sot, min, mak)
        app( str(res[0]) + " " + str(res[1]))

    print("\n".join(ans))

main()