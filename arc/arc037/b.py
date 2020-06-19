import sys

sys.setrecursionlimit(10**7)

def test():
    N, M = 100, 100*99//2
    G = [[] for _ in range(N + 1)]
    for i in range(1, 101):
        for j in range(1, 101):

            u, v = i, i+1
            G[u].append(v)
            G[v].append(u)
    return N, M, G

def m():
    # N, M = map(int, input().split())
    # G = [[] for _ in range(N + 1)]
    # for _ in range(M):
    #     u, v = map(int, input().split())
    #     G[u].append(v)
    #     G[v].append(u)
    N, M = 100, 100
    G = [[] for _ in range(N + 1)]
    def dfs(node, me, parent, is_tree):
        for n in node:
            if n == parent: continue
            if visited[n]: return False
            if not dfs(G[n], n, me, is_tree): return False
        return True

    ans = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        if dfs(G[i], i, None, True): ans += 1
    return ans


print(m())
