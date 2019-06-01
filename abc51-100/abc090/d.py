def m():
    n, k = map(int, input().split())
    ans = 0
    for b in range(1, n+1):
        p = n // b
        r = n % b
        ans += max(b-k, 0) * p
        ans += max(r-k+1, 0)
    if k == 0:
        ans -= n
    return ans

print(m())