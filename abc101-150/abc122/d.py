MOD = 10**9 + 7
N = int(input())

# dpがんばれ dp[100][4][4][4]が成功の近道
def m():
    if N == 3:
        return 4**N - 3
    if N >= 4:
        s = 4 ** N
        invalid = 3*4*(N-2) - 1*(N-3) + 3*(N-3)
        ans = s - invalid
        return ans % MOD

print(m())