def m():
    n = int(input())
    a = list(map(int, input().split()))
    even = a[1::2]
    odd = a[::2]
    ever_total = 0
    ans = 0
    if sum(even) > sum(odd):
        # マイナススタート
        for i in range(n):
            ever_total += a[i]
            if (i+2) % 2 == 0:
                if ever_total <= 0:
                    pass
                else:
                    ans += abs(a[i-1]) + 1
            else:
                if ever_total >= 0:
                    pass
                else:
                    ans += abs(a[i - 1]) + 1
    else:
        # プラス
        for i in range(n):
            ever_total += a[i]
            if (i+2) % 2 == 0:
                if ever_total >= 0:
                    pass
                else:
                    ans += abs(a[i-1]) + 1
            else:
                if ever_total <= 0:
                    pass
                else:
                    ans += abs(a[i - 1]) + 1
    return ans
print(m())