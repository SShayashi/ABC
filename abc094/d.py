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
        for k in range(i + 1, n):
            m = comb(v, a[k])
            if tmp < m:
                tmp = m
                ans = "{0} {1}".format(v, a[k])

    return ans


def ans():
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

    p = max(a)
    a.remove(p)
    tmp = 1
    tmpdiff = 9999999
    for i in a:
        if abs(tmpdiff - p / 2) > abs(i - p / 2):
            tmpdiff = i
            # diff = abs(i - want_near)
            # if diff == want_near:
            #     return "{0} {1}".format(p, i)
            # if diff < tmpdiff:
            #     tmpdiff = diff
            #     tmp = i

    return "{0} {1}".format(p, tmpdiff)


def someone_ans():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x_max = a[n - 1]
    center = a[0]
    for i in range(1, n - 1):
        if abs(center - x_max / 2) > abs(a[i] - x_max / 2):
            center = a[i]
    return "{0} {1}".format(x_max, center)


print(someone_ans())
