def m():
    n, k = map(int, input().split())
    grid = [[0]*(k*2) for _ in range(k*2)]
    for _ in range(n):
        x, y, c = map(str, input().split())
        x, y = int(x), int(y)
        grid[x % (k * 2)][((y+k) % (k * 2))] +=1
        # grid.append((x % (k * 2), (y+k) % (k * 2)))

    accum = [[0] * (k * 2) for _ in range(k * 2)]

    accum[0][0] = grid[0][0]
    # x軸
    for j in range(1, k*2):
        accum[j][0] = grid[j][0] + accum[j - 1][0]

    for i in range(1, k*2):
        accum[0][i] = grid[0][i] + accum[0][i - 1]

    for i in range(1, k*2):
        for j in range(1, k*2):
            accum[i][j] += grid[i][j] + accum[i][j-1] + accum[i-1][j] - accum[i-1][j-1]

    def query(sx, sy, gx, gy):
        return accum[gx][gy] - accum[sx][gy] - accum[gx][sy] + accum[sx][sy]

    ans = 0
    for i in range(k*2):
        for j in range(k*2):
            cnt = 0
            if i <= k and j <= k:
                pass
            if i == 0 and j == 0:
                pass
            if i == 0:
                pass
            if j == 0:
                pass
            ans = max(cnt, ans)
    pass


print(m())