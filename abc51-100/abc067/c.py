def m():
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()

    for i in range(1, n):
        b[i] = b[i] + b[i-1]
    for j in range(n-2, -1, -1):
        a[j] = a[j] + a[j+1]

    ans = 999999999999
    for j in range(n-1):
        ans = min(ans, abs(b[j] - a[j+1]))
    return ans
print(m())