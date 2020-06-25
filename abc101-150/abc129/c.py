def m():
    MOD = 10 ** 9 + 7
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    dp = [0] * (N + 1)
    for a in A: dp[a] = -1
    if N == 1:
        if dp[1] != -1:
            return 1
        else:
            return 0
    if dp[1] != -1 and dp[2] != -1:
        dp[1] = 1
        dp[2] = 2
    elif dp[1] != -1 and dp[2] == -1:
        dp[1] = 1
    elif dp[1] == -1 and dp[2] != -1:
        dp[2] = 1
    else:
        return 0

    for i in range(3, N + 1):
        if dp[i] == -1:
            continue
        l = dp[i - 2] if dp[i - 2] != -1 else 0
        r = dp[i - 1] if dp[i - 1] != -1 else 0
        dp[i] = (l + r) % MOD
    return dp[N] % MOD


print(m())
