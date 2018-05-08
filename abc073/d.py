import itertools


MAX = 999999999
def m():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    graph = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    def solve(d):
        for k in range(1,N+1):
            for j in range(1,N+1):
                for n in range(1,N+1):
                    d[j][n] = min(d[j][n], d[j][k] + d[k][n])
        return d

    e = solve(graph)
    ans = MAX
    for l in itertools.permutations(r):
        cost = 0
        for i in range(1,R):
            cost += e[l[i-1]][l[i]]
        ans = min(cost, ans)
    return ans
print(m())