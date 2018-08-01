def m():
    n, k = map(int, input().split())
    grid = [[0 for _ in range(k*2)] for _ in range(k*2)]
    for _ in range(n):
        x, y, c = map(str, input().split())
        x, y = int(x), int(y)
        if c == "W":
            grid[x % (k * 2)][(y+k) % (k * 2)] +=1
        else:
            grid[x % (k * 2)][y% (k * 2)] += 1
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
        if gx == -1 or gy == -1:
            return 0
        if sx == -1 and sy == -1:
            return accum[gx][gy]
        if sx == -1:
            return accum[gx][gy] - accum[gx][sy]
        if sy == -1:
            return accum[gx][gy] - accum[sx][gy]
        return accum[gx][gy] - accum[sx][gy] - accum[gx][sy] + accum[sx][sy]

    ans = 0
    MAX = k*2 -1
    MIN = -1
    for i in range(-1, MAX, 1):
        for j in range(-1, MAX, 1):
            cnt = 0
            cnt += query(i, j, min(i + k, MAX), min(j + k, MAX))
            cnt += query(min(i + k, MAX), max(j - k, MIN), min(i + k, MAX), min(j, MAX))
            cnt += query(min(i + k, MAX), min(j + k, MAX), min(i + k * 2, MAX), min(j + k * 2, MAX))
            cnt += query(max(i - k, MIN), min(j+k, MAX), i, min(j + k * 2, MAX))
            cnt += query(max(i-k, MIN), max(j-k, MIN), i, j)
            ans = max(cnt, ans)
    return ans

print(m())