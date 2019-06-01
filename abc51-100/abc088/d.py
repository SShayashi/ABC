MAX = 9999999
def m():
    h, w = map(int, input().split())
    s = []
    s.append(list(('#'*(w+2))))
    for j in range(h):
        s.append(list('#'+input()+'#'))
    s.append(list(('#' * (w + 2))))

    g = [[[] for _ in range(w+2)] for _ in range(h+2)]
    cnt = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if s[i][j] == '#':
                cnt +=1
                continue
            if s[i][j+1] == '.':
                g[i][j].append((i, j+1))
            if s[i+1][j] == '.':
                g[i][j].append((i+1, j))
            if s[i][j-1] == '.':
                g[i][j].append((i, j-1))
            if s[i-1][j] == '.':
                g[i][j].append((i-1, j))

    def dijkstra():
        d = [[MAX for _ in range(w + 2)] for _ in range(h + 2)]
        p = [[MAX for _ in range(w + 2)] for _ in range(h + 2)]
        visited = [[-1 for _ in range(w + 2)] for _ in range(h + 2)]
        d[1][1] = 0
        p[1][1] = -1
        while True:
            mincost = MAX
            for i in range(1, h + 1):
                for j in range(1, w + 1):
                    if visited[i][j] != 1 and d[i][j] < mincost:
                        mincost = d[i][j]
                        u = (i,j)
            if mincost == MAX:
                break
            visited[u[0]][u[1]] = 1

            for i in range(1, h + 1):
                for j in range(1, w + 1):
                    if visited[i][j] != 1 and u in g[i][j]:
                        if d[u[0]][u[1]] +1 < d[i][j]:
                            d[i][j] = d[u[0]][u[1]] + 1
                            p[i][j] = u
                            visited[i][j] = 0
        return d
    ans = dijkstra()
    if ans[h][w] == MAX:
        return -1
    return (w*h) - ans[h][w] - cnt -1

print(m())