def m():
    n, m = map(int, input().split())
    d = dict()
    yeard = dict()
    a = []
    b = []
    for i in range(m):
        p, y = map(int, input().split())
        a.append((p, y))
        b.append((p, y))

    a.sort(key=lambda x: x[1])
    for i in range(m):
        if d.get(a[i][0], 0) == 0:
            d[a[i][0]] = 1
            yeard[a[i][1]] = 1
        else:
            d[a[i][0]] += 1
            yeard[a[i][1]] = d[a[i][0]]

    for key, value in b:
        print(str(key).zfill(6)+str(yeard[value]).zfill(6))

m()