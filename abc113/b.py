def m():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    b = []
    diff = 10 ** 6
    ans = 0
    for i in range(n):
        tmp = t - h[i] * 0.006
        d = abs(tmp - a)
        b.append((d, i+1))
    b.sort(key=lambda x: x[0])
    return b[0][1]
print(m())