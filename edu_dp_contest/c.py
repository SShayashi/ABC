def main():
    n = int(input())
    a, b, c = [0] * n, [0] * n, [0] * n
    for i in range(n):
        x, y, z = map(int, input().split())
        a[i] = x
        b[i] = y
        c[i] = z
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b[i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c[i]
    return max(dp[n - 1])


print(main())
