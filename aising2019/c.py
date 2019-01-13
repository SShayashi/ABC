import sys
sys.setrecursionlimit(10**6)

def m():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))

    graph = [[[]for _ in range(W)] for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                continue
            if S[max(i - 1, 0)][j] == ".":
                graph[max(i - 1, 0)][j].append((i,j))
                graph[i][j].append((max(i - 1, 0),j))

            if S[min(i+1, H-1)][j] == ".":
                graph[min(i + 1, H - 1)][j].append((i,j))
                graph[i][j].append((min(i + 1, H - 1),j))

            if S[i][max(j - 1, 0)] == ".":
                graph[i][max(j - 1, 0)].append((i,j))
                graph[i][j].append((i,max(j - 1, 0)))

            if S[i][min(j+1, W-1)] == ".":
                graph[i][min(j + 1, W - 1)].append((i,j))
                graph[i][j].append((i,min(j+1, W-1)))

    bw = [0] * 2
    def dfs(g):
        for a,b in g:
            if visited[a][b] == 1:
                continue
            visited[a][b] = 1
            if S[a][b] == ".":
                bw[0] += 1
            else:
                bw[1] += 1
            dfs(graph[a][b])

    ans = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j] == 1:
                continue
            bw[0], bw[1] = 0, 0
            dfs(graph[i][j])
            ans += bw[0] * bw[1]

    return ans

print(m())