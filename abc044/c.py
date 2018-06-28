def m():
    n, a = map(int, input().split())
    x = list(map(int, input().split()))
    mm = max(x)
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n*mm)]
    dp[0][0][0] = 1
    for j in range(n):
        for k in range(n):
            for s in range(n*mm):
                if j == 0 and k == 0 and s == 0:
                    continue
                if j >= 1 and k >= 1 and s >= x[j]:
                    dp[j][k][s] = dp[j-1][k][s] + dp[]
                if j >= 1 and s < x[j]:
                    dp[j][k][s] = dp[j-1][j][s]

                pass
            pass
    pass

print(m())