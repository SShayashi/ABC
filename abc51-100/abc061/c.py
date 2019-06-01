def m():
    n, k = map(int, input().split())
    d = dict()
    for i in range(n):
        a, b = map(int, input().split())
        if d.get(a, 0) == 0:
            d[a] = b
        else:
            d[a] +=b
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        k -= d[key]
        if k <= 0:
            return key
print(m())