MOD = 10 ** 9 + 7


def main():
    s = str(input())
    l = len(s)
    dp = [[0 for _ in range(4)] for _ in range(l+1)]
    if l < 3:
        return 0
    abc = "ABC"
    dp[l][3] = 1
    for i in range(l, -1, -1):
        for j in range(3, -1, -1):
            if i == l:
                if j == 3:
                    dp[i][j] = 1
                if j < 3:
                    dp[i][j] = 0
                continue

            if i < l and j < 3:
                if s[i] == "?": m1 = 3
                else: m1 = 1
                if s[i] == "?" or s[i] == abc[j]:m2 = 1
                else: m2 = 0
                dp[i][j] = m1 * dp[i+1][j] + m2 * dp[i+1][j+1]
                continue

            if i < l:
                if s[i] == "?": m = 3
                else: m = 1
                dp[i][j] = dp[i+1][j] * m
                continue

    return dp[0][0] % MOD


print(main())
