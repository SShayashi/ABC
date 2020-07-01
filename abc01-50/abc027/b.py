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
        X.append(i)
        prev = 0
        f = True
        for x in X:
            if sum(A[prev:x]) % B != 0:
                f = False
                break
            if (sum(A[prev:x]) // len(A[prev:x])) != B:
                f = False
                break
            prev = x
        if not f: X.pop()
    return N-1 - len(X)

print(m())
