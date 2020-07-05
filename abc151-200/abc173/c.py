def m():
    H, W, K = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = 0
    for y in range(2 ** H):
        for x in range(2 ** W):
            y_mask = bin(y)[2:].zfill(H)
            x_mask = bin(x)[2:].zfill(W)
            black_cnt = 0
            for j in range(H):
                for i in range(W):
                    if y_mask[j] == '1':
                        continue
                    if x_mask[i] == '1':
                        continue
                    if G[j][i] == '#':
                        black_cnt += 1
            if black_cnt == K:
                ans += 1
    return ans


print(m())
