import bisect


def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = dict()
    CENTER = bisect.bisect_right(a, 0)
    maxixmum = a[n-1]
    minimum = a[0]
    left_side = CENTER
    right_side = n - CENTER

    if a[CENTER] == a[CENTER-1]:
        pass
    if a[CENTER] > a[CENTER-1]:
        pass

    for i in range(k):
        a[CENTER]
        pass

    pass


print(m())