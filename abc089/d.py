def m():
    h, w, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    pre = [0] * ((h*w)+1)
    for i in range(h):
        for j in range(w):
            pre[a[i][j]] = (i+1, j+1)
    accum = [0] * len(pre)
    for i in range(d+1, len(pre)):
        accum[i] = accum[i - d] \
                   + abs(pre[i][0] - pre[i - d][0])\
                   + abs(pre[i][1] - pre[i - d][1])

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        power = accum[r] - accum[l]
        print(power)

m()