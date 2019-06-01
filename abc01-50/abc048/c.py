def m():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = a.copy()
    ans = 0
    for i in range(n):
        if b[i] > x:
            b[i] = x

    for j in range(1, n):
        if b[j-1] + b[j] > x:
            b[j] -= (b[j-1] + b[j]) - x
        else:
            pass
    for k in range(n):
        ans += a[k] - b[k]
    return ans

print(m())