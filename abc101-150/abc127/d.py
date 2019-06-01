N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for _ in range(M):
    b, c = map(int, input().split())
    BC.append([b, c])


def m():
    A.sort()
    BC.sort(reverse=True, key=lambda x:x[1])
    i = 0
    j = 0
    while i < N:
        if A[i] > BC[j][1]:
            return sum(A)
        if BC[j][0] == 0:
            j += 1
            if len(BC) == j:
                return sum(A)
            continue
        A[i] = BC[j][1]
        BC[j][0] -= 1
        i += 1
    return sum(A)


print(m())