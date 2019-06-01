import copy


def m():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    E = []
    visited = []
    for i in range(M):
        a, b = map(int, input().split())
        E.append((a, b))

    for m in range(M):
        a, b = E[m]
        graph[a].append(b)
        graph[b].append(a)

    def dfs(v, g):
        if visited[v] == True:
            return
        visited[v] = True
        for i in g[v]:
            dfs(i, g)

    def is_all_visited(v):
        for i in range(1, N + 1):
            if v[i]:
                pass
            else:
                return False
        return True

    ans = 0
    for j in range(M):
        y, z = E[j]
        visited = [False] * (N + 1)
        tmp = copy.deepcopy(graph)
        tmp[y].remove(z)
        tmp[z].remove(y)
        dfs(1, tmp)
        if is_all_visited(visited):
            pass
        else:
            ans += 1

    return ans


print(m())
