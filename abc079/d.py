MAX = 999999

def fromto(i, j):

    pass

def solve(dp, A):
    nowcost = MAX
    for i in range(10):
        for j in range(10):
            A[i][j]
            pass
        pass
    return dp


def m():
    H, W = map(int, input().split())
    c = [[map(int, input().split()) for _ in range(10)] for _ in range(10)]
    A = [[map(int, input().split()) for _ in range(W)] for _ in range(H)]
    ans = [0 for _ in range(10)]
    dp = [[MAX] * 10 for _ in range(10)]
    for p in range(10):
        dp[p][p] = 0
        dp[p][1] = A[p][1]

    dp = solve(dp, A)

    for a in A:
        for i in a:
            if i != -1:
                ans[i] += 1

    pass


m()
