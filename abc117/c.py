N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

def m():
    a = [0] * M
    b = [0] * M
    for i in range(1, M):
        a[i] = abs(X[i] - X[i-1])
        b[i] = i

    if M <= N:
        return 0
    a.sort(reverse=True)
    for i in range(N-1):
        a[i] = 0

    return sum(a)


print(m())