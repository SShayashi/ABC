N = int(input())
xyr = [list(map(int, input().split())) for _ in range(N)]


def m():
    tmpx, tmpy, tmpr = 0, 0, 0
    for a,b,c in xyr:
        if c != 0:
            tmpx = a
            tmpy = b
            tmpr = c
            break

    for cx in range(0, 101):
        for cy in range(0, 101):
            h = max(0, tmpr + abs(tmpx - cx) + abs(tmpy - cy))
            f = 0
            for x, y, r in xyr:
                if not (r == max(h - abs(x - cx) - abs(y - cy), 0)):
                    f = 1
                    break
            if f == 0:
                return "{} {} {}".format(cx, cy, h)


print(m())