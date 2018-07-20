import bisect

MAXBIT = 29
def m():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    ans = 0
    for bit in range(MAXBIT):
        t = 2 ** (bit + 1)
        cnt = 0
        for i in range(n):
            tmp = t-a[i]
            left = bisect.bisect_left(b, t-a[i])
            right = bisect.bisect_right(b, t-a[i])
            cnt += len(b[left:right])
        ans += (cnt % 2) * (2 ** bit)
    return ans

print(m())