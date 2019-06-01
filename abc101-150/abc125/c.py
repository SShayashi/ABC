N = int(input())
A = list(map(int, input().split()))


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


def m():
    left, right = A.copy(), A.copy()
    for i in range(1, N):
        left[i] = gcd(A[i], left[i-1])

    for i in reversed(range(0, N-1)):
        right[i] = gcd(A[i], right[i+1])

    res = max(left[N-2], right[1])
    for i in range(1, N-1):
        res = max(gcd(left[i-1],right[i+1]), res)
    return res


print(m())
