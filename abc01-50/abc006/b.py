def m():
    n = int(input())
    MOD = 10007
    memo = [-1] * (10**6 +1)
    memo[0],memo[1],memo[2] = 0,0,0
    memo[3] = 1
    for i in range(4, n+1):
        memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % MOD
    return memo[n] %MOD
print(m())