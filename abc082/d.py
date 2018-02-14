def ans():
    s = input()
    x, y = map(int, input().split())
    dpx = [[0] * (len(s) * 2 + 2)] * abs(x + 1)
    dpy = [[0] * (len(s) * 2 + 2)] * abs(y + 1)
    CENTER = 8000
    dpx[0][CENTER] = True
    dpy[0][CENTER] = True

    head = 0
    xcnt = 1
    ycnt = 1
    i = 0
    while s[0] == 'F':
        s = s[1:]
        dpx[i][CENTER + 1] = True
        i += 1

    X_HEAD = 0
    Y_HEAD = 1
    # 最初はTになってるはず
    head = 0
    # xが連続で何回動いて，何回切り替わるかというのを数える必要がある（Yも同様）
    xcount = []
    ycount = []
    cnt = 0
    for i, v in enumerate(s):
        if v == 'F':
            cnt += 1
        else:
            if head == X_HEAD:
                xcount.append(cnt)
                head = Y_HEAD
                cnt = 0
            else:
                ycount.append(cnt)
                head = X_HEAD
                cnt = 0

    print(xcount,ycount)
    for i, v in enumerate(s):
        pass

    for i, v in enumerate(s):
        if v == 'F':
            if head == 0:
                for x in dpx[xcnt]:
                    pass
                dpx[xcnt] = dpx[xcnt - 1]
                xcnt += 1
            else:
                dpy[ycnt] = dpy[ycnt - 1]
                ycnt += 1
        if v == 'T':
            if head == 1:
                head = 0
            else:
                head = 1
    if dpx[abs(x)] and dpy[abs(y)]:
        return print('Yes')
    else:
        return print('No')


ans()
