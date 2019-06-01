import sys
sys.setrecursionlimit(10000000)

def m():
    def dfs(v, p, c, depth):
        depth[v] = c
        for child in graph[v]:
            if child == p:
                continue
            dfs(child, v, depth[v]+1, depth)
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    depth_from1 = [0] * (n+1)
    depth_fromN = [0] * (n+1)
    depth_from1[1] = 0
    depth_fromN[n] = 0

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1, -1, 0, depth_from1)
    dfs(n, -1, 0, depth_fromN)
    fene = 0
    sn = 0

    for i in range(1,n+1):
        if depth_from1[i] <= depth_fromN[i]:
            fene += 1
        else:
            sn += 1
    if fene > sn:
        return "Fennec"
    else:
        return "Snuke"


print(m())