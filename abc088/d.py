def m():
    h, w = map(int, input().split())
    s = []
    s.append('#'*(w+2))
    for j in range(h):
        s.append(list(map(int, str('# '+input()+ ' #').split())))
    s.append('#'*(w+2))

    g = [[0] * w for _ in range(h)]
    for i in range(w):
        for j in range(h):
            g[i][j] = 0
            pass
    pass

print(m())