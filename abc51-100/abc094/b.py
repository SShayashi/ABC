def m():
    N, M, X = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [0 for _ in range(N)]
    for a in A:
        B[a] = 1
    cost = min(sum(B[X:]), sum(B[:X]))
    return cost


print(m())
