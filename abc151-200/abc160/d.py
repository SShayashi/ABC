def m():
    N, X, Y = map(int, input().split())
    ans = [0] * (N+1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            p = min(abs(j - i), abs(X - i) + 1 + abs(Y - j), abs(Y - i) + 1 + abs(X - j))
            ans[p] += 1
    for a in range(1, N):
        print(ans[a]//2)

m()
