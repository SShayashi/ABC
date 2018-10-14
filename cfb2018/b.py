def m():
    n, x = map(int, input().split())
    ans = 0
    A,B = [],[]
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        ans += a*b
    ans += max(B) * x
    return ans

print(m())