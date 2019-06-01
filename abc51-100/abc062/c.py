def m():
    h, w = map(int, input().split())
    if h % 3 == 0 or w % 3 == 0:
        return 0
    ans = 9999999999

    for i in range(h):
        if ((h * w) - i * w) % 2 == 0:
            tmp = ((h * w) - i * w) // 2
            ans = min(ans, abs(tmp - (i * w)))
            continue
        c = ((h*w) - i*w) // (h - i)
        tmp = (c // 2) * (h - i)
        another = (c // 2 + 1) * (h - i)
        big = max(tmp, another, i*w)
        small = min(tmp, another, i*w)
        ans = min(ans, abs(big - small))

    for j in range(w):
        if ((h * w) - j*h) % 2 == 0:
            tmp = ((h * w) - j * h) // 2
            ans = min(ans, abs(tmp - (j * h)))
            continue
        c = ((h*w) - j*h) // (w - j)
        tmp = (c // 2) * (w - j)
        another = (c // 2 + 1) * (w - j)
        big = max(tmp, another, j*h)
        small = min(tmp, another, j*h)
        ans = min(ans, abs(big - small))

    return ans
print(m())