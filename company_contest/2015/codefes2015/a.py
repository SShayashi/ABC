def m():
    N, K, M, R = map(int, input().split())
    S = [int(input()) for _ in range(N-1)]
    S.sort(reverse=True)
    if sum(S[:K]) >= (R*K):
        return 0
    p = (R*K) - sum(S[:K-1])
    if 0 <= p <= M:
        return p
    elif p < 0:
        return 0
    else:
        return -1



print(m())