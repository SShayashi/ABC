import bisect


def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [abs(i) for i in a]
    right = bisect.bisect_right(a,0)
    left = right-1
    ans = 99999999999
    for i in range(n-k+1):
        s = 0
        if left >= i+k-1:
            s = b[i]
        elif right <= i:
            s = b[i+k-1]
        else:
            s = min(b[i] + b[i+k-1]*2, b[i]*2 + b[i+k-1])
        ans = min(ans, s)
    return ans

print(m())