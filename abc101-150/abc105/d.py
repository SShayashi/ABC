import math


def m():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    ans = 0
    for i in range(1, n):
        b[i] = b[i-1] + a[i]
    d = dict()
    d[0] = 1
    for i in range(n):
        t = d.get(b[i]%m, 0)
        d[b[i]%m] = t+1
    for v in d.values():
        if v < 2:
            continue
        ans += math.factorial(v) // (math.factorial(v-2) * 2)
    return ans

print(m())