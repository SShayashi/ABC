MAX = 99999999


def solve(dp):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


def m():
    H, W = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = [0 for _ in range(10)]
    # dp = [[MAX] * 10 for _ in range(10)]
    c = solve(c)

    for a in A:
        for i in a:
            if i != -1:
                ans[i] += 1

    cost = 0
    for i in range(10):
        cost += c[i][1] * ans[i]
    return cost


print(m())
