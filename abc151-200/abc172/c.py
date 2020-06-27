import bisect


def m():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    AR = [0] * (N + 1)
    BR = [0] * (M + 1)
    for i in range(N):
        AR[i + 1] = AR[i] + A[i]
    for i in range(M):
        BR[i + 1] = BR[i] + B[i]

    ai = bisect.bisect_right(AR, K)
    for a in range(ai-1, -1, -1):
        bk = K - AR[a]
        bi = bisect.bisect_right(BR, bk)

        ans = max(a + bi - 1, ans)
    return ans


print(m())
