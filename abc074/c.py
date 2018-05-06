def m():
    A, B, C, D, E, F = map(int, input().split())

    tmp = 0
    ans = ""
    for i in range(F):
        for k in range(F):
            x = A * 100 * i + B * 100 * k
            y = C * i + D * k
            if x + y > F:
                continue
            if i + k == 0:
                continue
            if y > (x // 100) * E:
                continue
            if tmp < (100 * x) // (x + y):
                tmp = (100 * x) // (x + y)
                ans = "{0} {1}".format(x + y, y)
    return ans


def someone_ans():
    a, b, c, d, e, f = map(int, input().split())
    water = []
    sugar = []
    ans_1, ans_2, con = 0, 0, 0
    for i in range(f // 100 + 1):
        for k in range(f // 100 + 1):
            x = 100 * a * i + 100 * k * b
            if 0 < x <= f:
                water.append(x)
    for i in range(f):
        for k in range(f):
            y = c * i + d * k
            if y <= f:
                sugar.append(y)
    sugar = list(set(sugar))
    for w in water:
        for s in sugar:
            if w + s <= f:
                if s <= w // 100 * e:
                    now = (100 * s) / (s + w)
                    if con <= now:
                        ans_1 = s + w
                        ans_2 = s
                        con = now
    return "{0} {1}".format(ans_1, ans_2)


# print(m())

print(someone_ans())
