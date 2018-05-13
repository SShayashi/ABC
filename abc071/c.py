def m():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    edge = []
    tmp = 0
    for i in range(N):
        if A[i] == tmp:
            edge.append(tmp)
            tmp = 0
        else:
            tmp = A[i]
    if len(edge) < 2:
        return 0
    else:
        return edge[-1] * edge[-2]

print(m())