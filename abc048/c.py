def m():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        d = a[i]+a[i-1] - x
        if d <= 0:
            ad = abs(a[i] - a[i-1])
            if abs(d) < abs(ad):
                if a[i] > a[i-1]:
                    a[i] -= d
                    ans += d
                else:
                    a[i-1] -=d
                    ans += d
            else:
                if a[i] > a[i-1]:
                    a[i] -=ad
                    ans += ad
                    z = abs(d) - ad
                    if z % 2 == 0:
                        a[i] -= z//2
                        a[i-1] -= z//2
                        ans += z
                        continue

                    a[i] -= z//2
                    a[i-1] -= (z//2 + 1)
                    ans +=z
                else:
                    a[i-1] -=ad
                    ans += ad
                    z = abs(d) - ad
                    if z % 2 == 0:
                        a[i] -= z//2
                        a[i-1] -= z//2
                        ans += z
                        continue
                    a[i] -= z//2
                    a[i-1] -= (z//2+1)
                    ans +=z
    return ans


print(m())