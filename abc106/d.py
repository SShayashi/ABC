def m():
    n, M, Q = map(int, input().split())
    L, R = 0, 1
    a = [[0 for _ in range(n+1)] for _ in range(2)]
    for i in range(M):
        l, r = map(int, input().split())
        a[L][l] += 1
        a[R][r] += 1
    b = [[0 for _ in range(n+1)] for _ in range(2)]

    for i in range(2):
        for j in range(1, n+1):
            b[i][j] = a[i][j] + b[i][j-1]

    for i in range(Q):
        p, q = map(int, input().split())
        left = b[L][p-1]
        right = b[R][q] - b[R][p]
        print(right-left)
m()