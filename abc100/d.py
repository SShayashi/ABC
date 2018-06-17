def main():
    n, m = map(int, input().split())
    a = []
    f = [-1, 1]
    for _ in range(n):
        x, y, z = map(int, input().split())
        a.append((x,y,z))
    ans = 0
    for i in f:
        for k in f:
            for p in f:
                a.sort(key=lambda t: t[0] * i +t[1] * k +t[2] * p)
                sx = 0
                sy = 0
                sz = 0
                for j in range(m):
                    sx += a[j][0]
                    sy += a[j][1]
                    sz += a[j][2]
                s = abs(sx) + abs(sy) + abs(sz)
                ans = max(ans, s)
    return ans


print(main())