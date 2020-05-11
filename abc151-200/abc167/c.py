import itertools


def m():
    N, M, X = map(int, input().split())
    CA = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    for i in itertools.product([True, False], repeat=N):
        tmp = [0] * (M + 1)
        for j, v in enumerate(i):
            if v:
                for k in range(M + 1):
                    tmp[k] += CA[j][k]
        f = 1
        for p in range(1, M + 1):
            if tmp[p] < X: f = 0
        if f: ans = min(ans, tmp[0])
    return ans if ans != float('inf') else "-1"


print(m())
