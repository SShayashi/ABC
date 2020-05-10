def m():
    N, M, X = map(int, input().split())
    CA = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    for i in range(2 ** N):
        b = bin(i)[2:]
        b = b.zfill(N)
        tmp = [0] * (M + 1)
        for j, v in enumerate(b):
            if v == '0':
                continue
            tmp[0] += CA[j][0]
            for k in range(1, M + 1):
                tmp[k] += CA[j][k]
        f = 1
        for p in range(1, M + 1):
            if tmp[p] < X:
                f = 0
                break
        if f == 0:
            continue
        ans = min(ans, tmp[0])
    if ans == float('inf'):
        return '-1'
    else:
        return ans


print(m())
