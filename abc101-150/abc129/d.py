def m():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    Gx = [[-1 for _ in range(W)] for _ in range(H)]
    Gy = [[-1 for _ in range(W)] for _ in range(H)]

    for a in range(H):
        left = 0
        for b in range(W):
            if S[a][b] == '#':
                left = 0
            else:
                Gx[a][b] = left + 1
                left = Gx[a][b]
    for b in range(W):
        top = 0
        for a in range(H):
            if S[a][b] == '#':
                top = 0
            else:
                Gy[a][b] = top + 1
                top = Gy[a][b]

    for i in reversed(range(H)):
        right = 0
        for j in reversed(range(W)):
            if Gx[i][j] == -1:
                right = 0
            else:
                Gx[i][j] = max(Gx[i][j], right)
                right = Gx[i][j]

    for j in reversed(range(W)):
        bot = 0
        for i in reversed(range(H)):
            if Gy[i][j] == -1:
                bot = 0
            else:
                Gy[i][j] = max(Gy[i][j], bot)
                bot = Gy[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(Gx[i][j] + Gy[i][j], ans)
    return ans - 1


print(m())

'''
以下を参考にTLE→AC

https://juppy.hatenablog.com/entry/2019/06/14/Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E9%AB%98%E9%80%9F%E5%8C%96tips_%28Python%E3%81%A7Atcoder%E3%82%92%E3%82%84%E3%82%8B%E9%9A%9B%E3%81%AB%E5%80%8B
⑥配列をできるだけ軽くする
軽くするというのは次元的な意味でも処理的な意味でもです。
基本的にPythonで定数倍の為にTLEするのは配列関連です。
　
よくある手法は「三次元の配列を二次元の配列何個かにする」というものです。
例えばDPで
　dp[i][j][k] = dp[i-1][j-1][k-1]*dp[i-1][j][[k]%mod
みたいな遷移があった時、これを3次元DPで実装するのではなく、下のように2次元配列二つで実装します。
　
'''