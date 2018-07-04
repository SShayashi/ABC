def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    times = 1
    for i in range(n):
        ans += a[i] * times
        if i < k-1:
            times += 1
        if i >= n-k:
            times -= 1
    return ans
print(m())