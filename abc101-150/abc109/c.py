def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


def m():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n

    for i in range(n):
        b[i] = abs(x - a[i])

    tmp = b[0]
    for i in range(n):
        tmp = gcd(tmp, b[i])

    return tmp

print(m())