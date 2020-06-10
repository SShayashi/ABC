def m():
    X, Y, W = map(str, input().split())
    X, Y = map(int, (X, Y))
    C = [list(input()) for _ in range(9)]
    a, b = [X-1] * 4, [Y-1] * 4
    if 'R' in W:
        flag = False
        for i in range(1, 4):
            if a[i - 1] == 8: flag = True
            a[i] = a[i - 1] - 1 if flag else a[i - 1] + 1
    if 'L' in W:
        flag = False
        for i in range(1, 4):
            if a[i - 1] == 0: flag = True
            a[i] = a[i - 1] + 1 if flag else a[i - 1] - 1

    if 'U' in W:
        flag = False
        for i in range(1, 4):
            if b[i - 1] == 0: flag = True
            b[i] = b[i - 1] + 1 if flag else b[i - 1] - 1

    if 'D' in W:
        flag = False
        for i in range(1, 4):
            if b[i - 1] == 8: flag = True
            b[i] = b[i - 1] - 1 if flag else b[i - 1] + 1
    ans = ''
    for i in range(4):
        ans += C[b[i]][a[i]]
    return ans


print(m())
