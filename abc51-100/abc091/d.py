import bisect

MAXBIT = 29
def m():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for bit in range(MAXBIT):
        t = 2 ** bit
        cnt = 0
        A = [0] * n
        B = [0] * n
        for i in range(n):
            A[i] = a[i] % (t * 2)
            B[i] = b[i] % (t * 2)
        B.sort()
        for i in range(n):
            left = bisect.bisect_left(B, t*1-A[i])
            right = bisect.bisect_right(B, (t*2-A[i])-1)
            cnt += right-left

            left = bisect.bisect_left(B, t*3-A[i])
            right = bisect.bisect_right(B, (t*4-A[i])-1)
            cnt += right-left

        ans += (cnt % 2) * t
    return ans

print(m())