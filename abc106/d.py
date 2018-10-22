def m():
    n, M, Q = map(int, input().split())
    a = [[0 for _ in range(n+1)] for _ in range(n+1)]
    b = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(M):
        l, r = map(int, input().split())
        a[l][r] += 1

    for i in range(1, n+1):
        b[1][i] += a[1][i] + b[1][i-1]
    for i in range(2, n+1):
        b[i][1] += a[i][1] + b[i-1][1]

    for i in range(1, n+1):
        for j in range(1, n+1):
            b[i][j] = a[i][j] + b[i-1][j] + b[i][j-1] - b[i-1][j-1]

    for i in range(Q):
        p, q = map(int, input().split())
        ans = b[q][q] + b[p-1][p-1] - b[q][p-1] - b[p-1][q]
        print(ans)

m()