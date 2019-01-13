def m():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    total = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                continue
            if S[max(i - 1, 0)][j] == ".":
                total[max(i - 1, 0)][j] += 1

            if S[min(i+1, H-1)][j] == ".":
                total[min(i + 1, H - 1)][j] += 1

            if S[i][max(j - 1, 0)] == ".":
                total[i][max(j - 1, 0)] += 1

            if S[i][min(j+1, W-1)] == ".":
                total[i][min(j + 1, W - 1)] += 1

    return total

print(m())