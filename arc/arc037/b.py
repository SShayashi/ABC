import sys

sys.setrecursionlimit(10**7)

flag = True
def m():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    visited = [False] * (N + 1)

    def dfs(me, parent):
        global flag
        for n in G[me]:
            if n == parent: continue
            if visited[n]:
                flag = False
            else:
                visited[n] = True
                dfs(n, me)
    ans = 0
    for i in range(1, N + 1):
        global flag
        flag = True
        if visited[i]:
            continue
        dfs(i, None)
        if flag: ans += 1
    return ans


print(m())
