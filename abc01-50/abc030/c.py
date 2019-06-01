import bisect

def m():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    time = 0
    limit = max(b) + 1
    ans = 0
    while time < limit:
        if bisect.bisect_left(a,time) == n:
            break
        time = max(time,a[bisect.bisect_left(a,time)]) + x
        if time >= limit:
            break
        if bisect.bisect_left(b,time) == m:
            break
        time = max(time,b[bisect.bisect_left(b,time)]) + y
        ans += 1
    return ans

print(m())
