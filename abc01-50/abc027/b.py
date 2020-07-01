def m():
    N = int(input())
    A = list(map(int, input().split()))
    SUM = sum(A)
    if SUM % N != 0:
        return -1
    B = SUM // N
    X = [True] * N
    for i in range(1, N):
        tmp = [0,0]
        f = True
        for j in range(N):
            if j == i or not X[j]:
                avr = tmp[0] // tmp[1]
                if avr != B:
                    f = False
                tmp = [0, 0]
                continue

            tmp[0] += A[j]
            tmp[1] +=1
        avr = tmp[0] // tmp[1]
        if avr != B: f = False
        if f: X[i] = False

    return N - 1 - X.count(False)


print(m())
