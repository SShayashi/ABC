def m():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    X = [0] * (N+1)
    for i in range(N, 0,-1):
        p = 0
        for j in range(i, N+1, i):
            if X[j]: p +=1
        if p % 2 != A[i]:
            X[i] = 1
    M = X.count(1)
    print(M)
    for i in range(1, N+1):
        if X[i] == 0:
            continue
        print(i, end=' ')
    return

m()