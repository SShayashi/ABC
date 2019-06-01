# 理解できてないので後で復習

def others_ans01():
    s = input()
    x, y = map(int, input().split())
    L = len(s)
    dpx = set()
    dpy = set()
    xs = []
    ys = []
    tmp = 0
    d = 0
    for c in s:
        if c == 'F':
            tmp += 1
            continue

        if c == 'T':
            if tmp:
                if d == 0:
                    xs.append(tmp)
                else:
                    ys.append(tmp)
            d ^= 1
            tmp = 0
    if tmp:
        if d == 0:
            xs.append(tmp)
        else:
            ys.append(tmp)

    if s[0] == 'F':
        dpx.add(xs[0])
        xs = xs[1:]
    else:
        dpx.add(0)
    dpy.add(0)

    for a in xs:
        tmp = set()
        for dx in dpx:
            tmp.add(dx + a)
            tmp.add(dx - a)
        dpx = tmp
    for a in ys:
        tmp = set()
        for dy in dpy:
            tmp.add(dy + a)
            tmp.add(dy - a)
        dpy = tmp
    if x in dpx and y in dpy:
        print('Yes')
    else:
        print('No')


def others_asn02():
    def check_x(moving):
        n = sum(moving[::2])
        dpx = [False] * L
        dpx[moving[0]+n] = True
        for m in moving[2::2]:
            if m == 0: continue
            n_move = dpx[m:] + [False] * m
            p_move = [False] * m + dpx[:-m]
            t = [a or b for a, b in zip(n_move, p_move)]
            dpx = t
        return dpx,n

    def check_y(moving):
        n = sum(moving[1::2])
        dpy = [False] * (n * 2 + 1)
        dpy[n] = True
        for f in moving[1::2]:
            if f == 0:continue
            n_move = dpy[f:] + [False] * f
            p_move = [False] * f + dpy[:-f]
            t = [a or b for a, b in zip(n_move, p_move)]
            dpy = t
        return dpy, n

    s = input()
    x, y = map(int, input().split())
    L = len(s) * 2 + 2
    moves = [len(x) for x in s.split('T')]
    dpx, cx = check_x(moves)
    dpy, cy = check_y(moves)

    if cx < abs(x): return print('No')
    if cy < abs(y): return print('No')
    if dpx[x + cx] is True and dpy[y + cy] is True:
        return print('Yes')
    else:
        return print('No')



def ans():
    s = input()
    x, y = map(int, input().split())
    L = len(s) * 2 + 2
    dpx = [False] * L
    dpy = [False] * L

    CENTER = len(s)
    # dpx[center][0] = tue

    head = 0
    xcnt = 1
    ycnt = 1
    m = 0
    while s[0] == 'F':
        s = s[1:]
        m += 1
        dpx[CENTER + m][m] = True

    X_HEAD = 0
    Y_HEAD = 1
    splited = s.split('F')
    head = 1

    x_fs = splited[0:2]
    y_fs = splited[1:2]

    for i in enumerate(x_fs):
        pass
    s = s[1:]
    # 最初はTになってるはず
    head = Y_HEAD
    # xが連続で何回動いて，何回切り替わるかというのを数える必要がある（Yも同様）
    xcount = []
    ycount = []
    cnt = 0

    for i, v in enumerate(s):
        if v == 'F':
            cnt += 1
        else:
            if head == X_HEAD:
                dpx[CENTER]
                xcount.append((cnt, i + m))  # 連続で増える数，何回目か
                head = Y_HEAD
                cnt = 1
            else:
                ycount.append((cnt, i + m))
                head = X_HEAD
                cnt = 1

    for increments, c in xcount:
        num = c - increments
        for i in range(increments):
            dpx[CENTER + i][num + i] = True
            dpx[CENTER + -i][num + i] = True

    for increments, c in ycount:
        num = c - increments
        for i in range(increments):
            dpy[CENTER + i][num + i] = True
            dpy[CENTER + -i][num + i] = True

    if dpx[abs(x)] and dpy[abs(y)]:
        return print('Yes')
    else:
        return print('No')

# ans()
# others_ans01()
others_asn02()
