def m():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    G = [[[-1, -1] for _ in range(W)] for _ in range(H)]
    for a in range(H):
        left = 0
        for b in range(W):
            if S[a][b] == '#':
                left = 0
            else:
                G[a][b][0] = left + 1
                left = G[a][b][0]
    for b in range(W):
        top = 0
        for a in range(H):
            if S[a][b] == '#':
                top = 0
            else:
                G[a][b][1] = top + 1
                top = G[a][b][1]

    for i in reversed(range(H)):
        right = 0
        for j in reversed(range(W)):
            if G[i][j][0] == -1:
                right = 0
            else:
                G[i][j][0] = max(G[i][j][0], right)
                right = G[i][j][0]

    for j in reversed(range(W)):
        bot = 0
        for i in reversed(range(H)):
            if G[i][j][1] == -1:
                bot = 0
            else:
                G[i][j][1] = max(G[i][j][1], bot)
                bot = G[i][j][1]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(sum(G[i][j]), ans)
    return ans-1


print(m())
