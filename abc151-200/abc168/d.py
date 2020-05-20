from collections import deque

def m():
    N, M = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    dp = [10 ** 9] * (N + 1)
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    list()
    def bfs(root):
        visited[root] = True
        dp[root] = 0
        queue = deque([])
        for q in g[root]:
            dp[q] = root
            queue.append(q)
            visited[q] = True
        while queue:
            q = queue.popleft()
            for k in g[q]:
                if not visited[k]:
                    queue.append(k)
                    dp[k] = q
                    visited[k] = True
    bfs(1)

    if not all(visited[2:]):
        print('No')
        return

    print('Yes')
    for j in dp[2:]:
        print(j)
    return

m()
