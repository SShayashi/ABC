def m():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1, 2):
        if a[i+1] > a[i-1]:
            if a[i+1] + a[i] < x:
                continue
            ans += (a[i+1] + a[i]) -x
            if a[i+1] > x:
                a[i+1] = x

        else:
            if a[i-1] + a[i] < x:
                continue
            ans += (a[i-1] + a[i]) -x
    if len(a) % 2 == 0:
        if a[-1] + a[-2] < x:
            return ans
        ans += (a[-1] + a[-2]) -x
        return ans
    else:
        return ans

print(m())