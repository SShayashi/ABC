def m():
    W = 11
    S = []
    S.append(list('xxxxxxxxxxxx'))
    iland_cnt = 0
    for _ in range(W - 1):
        iland = list('x' + input() + 'x')
        iland_cnt += iland.count('o')
        S.append(iland)
    S.append(list('xxxxxxxxxxxx'))

    G = [[[] for _ in range(W + 1)] for _ in range(W + 1)]
    AREA = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    for j in range(1, W):
        for i in range(1, W):
            if S[j][i] == 'x':
                continue
            for x, y in AREA:
                if S[j + y][i + x] == 'o':
                    G[j][i].append([j + y, i + x])
                    G[j + y][i + x].append([j, i])

    visited = [[False] * (W + 1) for _ in range(W + 1)]

    def dfs(root):
        for x, y in root:
            if visited[x][y]:
                continue
            visited[x][y] = True
            dfs(G[x][y])

    def is_all_visited(visited):
        tmp = 0
        for a in range(1, W):
            for b in range(1, W):
                if visited[a][b]:
                    tmp += 1
        return tmp >= iland_cnt

    for j in range(1, W):
        for i in range(1, W):
            visited = [[False] * (W + 1) for _ in range(W + 1)]
            tmp = []
            for x, y in AREA:
                if S[j + x][i + y] != 'x':
                    tmp.append([j + x, i + y])
            dfs(tmp)
            if is_all_visited(visited):
                return 'YES'
    return 'NO'


print(m())
