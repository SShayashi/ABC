def m():
    N = int(input())
    A = list(map(int, input().split()))
    SUM = sum(A)
    if SUM % N != 0:
        return -1
    B = SUM // N
    if B == 0:
        if sum(A) == 0:
            return 0
        else:
            return -1

    X = []
    for i in range(1, N):
        if sum(A[:i]) // len(A[:i]) != B:
            X.append(i)
            continue
        if sum(A[i:]) // len(A[i:]) != B:
            X.append(i)
            continue
    return len(X)

print(m())
