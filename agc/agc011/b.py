def m():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i - 1] + A[i]
    prob = 0
    for i in range(N - 1):
        if B[i] * 2 < A[i + 1]:
            prob = 0
            continue
        prob += 1
    return prob+1


print(m())
