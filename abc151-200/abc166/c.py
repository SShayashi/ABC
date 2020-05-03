def m():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = 0
    for i in range(1, N+1):
        current = H[i-1]
        p = 1
        for x in graph[i]:
            if current <= H[x-1]:
                p = 0
                break
        ans += p
    return ans


print(m())
