def m():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        a.append((x, y, z))
    xsum = 0
    ysum = 0
    zsum = 0
    for i in range(n):
        xsum += a[i][0]
        ysum += a[i][1]
        zsum += a[i][2]

    pass

print(m())