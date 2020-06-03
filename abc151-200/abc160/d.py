import queue
def m():
    N, X, Y = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(1, N):
        G[i].append(i+1)
        G[i+1].append(i)
    G[X].append(Y)
    G[Y].append(X)
    q = queue.Queue()
    X = [-1] * (N+1)
    def bfs(i):
        visited = [False] * (N + 1)
        arr = X.copy()
        arr[i] = 0
        visited[i] = True
        for j in G[i]:
            q.put((j, 1))
        while not q.empty():
            d,dist = q.get()
            if visited[d]: continue
            visited[d] = True
            arr[d] = dist
            for k in G[d]:
                if visited[k]: continue
                q.put((k, dist+1))
        return arr
    calc = [bfs(i) for i in range(1, N+1)]
    done = [[False]*(N+1) for _ in range(N+1)]
    for i in range(1, N):
        ans = 0
        tmp = done.copy()
        for j in calc[i]:
            if j == i:
                if tmp[i][j] or tmp[j][i]:
                    continue
                tmp[i][j] = True
                tmp[j][i] = True
                ans += 1
        print(ans)

m()