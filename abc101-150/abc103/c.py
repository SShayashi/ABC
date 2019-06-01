def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


def m():
    n = int(input())
    a = list(map(int, input().split()))
    tmp = a[0]
    ans = 0
    modv = tmp
    for i in range(1, n):
        tmp = gcd(modv, a[i])
        modv = (modv*a[i] // tmp)
    for i in range(n):
        ans += (modv-1) % a[i]
    return ans
print(m())