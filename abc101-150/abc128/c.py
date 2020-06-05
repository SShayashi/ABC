def m():
    N, M = map(int, input().split())
    K = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for b in range(1 << N):
        mask = bin(b)[2:].zfill(N)
        light = [False] * M
        for j in range(M):
            on = 0
            for k in range(1, K[j][0] + 1):
                if mask[K[j][k] - 1] == '1':
                    on += 1
            if (on % 2) == P[j]:
                light[j] = True
        if all(light):
            ans += 1
    return ans


print(m())
