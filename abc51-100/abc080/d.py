def m():
    N, C = map(int, input().split())
    s = []
    t = []
    c = []
    for i in range(N):
        x, y, z = map(int, input().split())
        s.append(x)
        t.append(y)
        c.append(z)

    TIME = 100002
    recod = [[0 for _ in range(1, TIME+1)] for _ in range(1, C+2)]
    for n in range(N):
        for k in range(s[n], t[n]+1):
            recod[c[n]][k] = 1

    recodcnt = 1
    for n in range(TIME):
        tmp = 0
        for g in range(1, C+1):
            if recod[g][n] == 1:
               tmp += 1
        recodcnt = max(tmp, recodcnt)
    return recodcnt


print(m())