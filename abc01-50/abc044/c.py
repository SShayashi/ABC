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
                    dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j]]
                if j >= 1 and s < x[j]:
                    dp[j][k][s] = dp[j-1][j][s]

                dp[j][k][s] = 0
                pass
            pass
    pass


def someone_ans():
    n, a = map(int, input().split())
    cards = list(map(int, input().split()))
    cards.append(0)
    W = sum(cards)
    # dp[j][k][s]: j番目までのカードをk枚使って合計をsにする組み合わせ
    dp = [[[0] * (W+1) for _ in range(n+1)] for _ in range(n+1)]
    for j in range(n+1):
        dp[j][0][0] = 1

    for j in range(1, n+1):
        card = cards[j]
        for k in range(1,n+1):
            for s in range(1, W+1):
                if s < card:
                    dp[j][k][s] = dp[j-1][k][s]
                else:
                    dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-card]
    ans = 0
    for k in range(1, n+1):
        if k*a <= W:
            ans += dp[n][k][k*a]
    return ans


print(m())