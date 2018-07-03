def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    ans = 0
    for i in range(n-k+1):
        for j in range(k):
            b[i+j] +=1
    for i in range(n):
        ans += a[i]*b[i]
    return ans
print(m())