def ans():
    N = int(input())
    A = list(map(int, input().split()))
    result = []
    MAX = max(A)
    MAX_INDEX = A.index(MAX)
    MIN = min(A)
    MIN_INDEX = A.index(MIN)

    if abs(MAX) > abs(MIN):
        # B = [a + MAX for a in A]
        B = []
        for i, v in enumerate(A):
            b = v + MAX
            B.append(b)
            result.append((MAX_INDEX, i))

        for i in range(N):
            if i == 0: continue
            B[i] = B[i] + B[i - 1]
            result.append((i - 1, i))
    else:
        B = []
        for i, v in enumerate(A):
            b = v + MIN
            B.append(b)
            result.append((MIN_INDEX, i))

        for i in range(N - 1, -1, -1):
            if i == N-1: continue
            B[i] = B[i] + B[i + 1]
            result.append((i + 1, i))

    print(len(result))
    for r in result:
        print(r[0]+1, r[1]+1)


ans()
