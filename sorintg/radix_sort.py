
def radix(list):
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



list = [123,5323,3456,8765,45,9,3435]


print ', '.join(str(x) for x in list)
list = radix(list)
print ', '.join(str(x) for x in list)

