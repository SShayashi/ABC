def m():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    visited = [[] for _ in range(n + 1)]
    visited[1].append(0)
    cur = 1
    i = 1
    while True:
        cur = a[cur]
        visited[cur].append(i)
        i += 1
        if len(visited[cur]) >= 2:
            break

    if k <= visited[cur][0]:
        now = 1
        for p in range(1, k+1):
            now = a[now]
        return now
    else:
        tmp = k - visited[cur][0]
        MOD = visited[cur][1] - visited[cur][0]
        count = tmp % MOD
        now = 1
        for p in range(1, count+1+visited[cur][0]):
            now = a[now]
        return now


print(m())
