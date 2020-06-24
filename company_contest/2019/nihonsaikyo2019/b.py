def m():
    MOD = 10 ** 9 + 7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if len(A) == 1:
        return 0
    l2r = 0
    for i in range(N):
        prev = A[i]
        for j in range(i, N):
            if prev > A[j]:
                l2r += 1
    r2l = 0
    for i in range(N - 1, -1, -1):
        prev = A[i]
        for j in range(i, -1, -1):
            if prev > A[j]:
                r2l += 1

    ans1 = K * (K + 1) // 2 * l2r % MOD
    ans2 = (K - 1) * K // 2 * r2l % MOD
    return (ans1 + ans2) % MOD


print(m())
