def m():
    n, T = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        diff = abs(t[i-1] - t[i])
        if diff <= T:
            ans += diff
            continue
        ans += T
    ans += T
    return ans


print(m())