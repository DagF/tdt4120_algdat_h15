def main():
    from sys import stdin



    def minCoinsGreedy(coins, value):
        c = 0
        i = 0
        cs = len(coins)
        while value > 0:
            if value >= coins[i]:
                value -= coins[i]
                c += 1
            else:
                if i < cs:
                    i += 1

        return c



    def minCoinsDynamic(coins):
        values = []
        v_a = values.append
        for line in stdin:
            v_a(int(line))

        m_v = max(values)

        cs = [100000] * (m_v + 1) #Array with space for all values from 0 to max

        for c in coins:
            if c <= m_v:
                cs[c] = 1

        cs[0] = 0

        for i in range(1,(m_v + 1)):

            cs[i] = min(
              cs[i],
                    min([cs[i-j] for j in coins if j <= i]
                                ) + 1
            )

        a = []
        a_a = a.append
        for v in values:
            a_a(str(cs[v]))

        print("\n".join(a))




    def canUseGreedy(coins):
        m = len(coins) - 1
        for i in range(0, m+1):
            for j in range(0, m+1):
                if coins[i] + coins[j] > coins[m] and minCoinsGreedy(coins, coins[i] + coins[j]) > 2:
                    return False

        return True






    coins = []
    c_a = coins.append
    for c in stdin.readline().split():
        c_a(int(c))

    coins.sort()
    coins.reverse()
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
        e = []
        e_a = e.append
        for line in stdin:
            e_a( str(minCoinsGreedy(coins, int(line))))

        print( "\n".join(e) )
    else:
        minCoinsDynamic(coins)

main()