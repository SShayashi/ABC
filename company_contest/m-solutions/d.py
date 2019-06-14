score = 0

def m():
    N = int(input())
    g = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    C = list(map(int, input().split()))
    C.sort(reverse=True)
    nodes = {}

    for i in range(1, N+1):
        nodes[i] = len(g[i])
    l = list(nodes.items())
    l.sort(reverse=True, key=lambda x:x[1])
    ans = [0] * N
    for k,v in l:
        ans[k-1] = C[k-1]

    visited = [False] * (N+1)
    def dfs(v, g):
        if visited[v] == True:
            return
        visited[v] = True
        for i in g[v]:
            global score
            score += min(ans[i-1], ans[v-1])
            dfs(i, g)
    dfs(1,g)
    print(score//2)
    return ans

print(*m())