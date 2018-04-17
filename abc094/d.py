def m():
    n = int(input())
    a = list(map(int, input().split()))

    def comb(x, y):
        c = 1
        p = 1
        for i in range(y, 0, -1):
            c = c * i
        for i in range(x, x - y, -1):
            p = p * i
        return p / c

    a.sort(reverse=True)
    tmp = 0
    ans = ""
    for i, v in enumerate(a):
        for k in range(i+1, n):
            m = comb(v, a[k])
            if tmp < m:
                tmp = m
                ans = "{0} {1}".format(v, a[k])

    return ans


print(m())
