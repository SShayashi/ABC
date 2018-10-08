def m():
    n, m = map(int, input().split())
    g = []
    for _ in range(m):
        a, b = map(int, input().split())
        flag = 0
        for p in g:
            if a >= p[0] and b <= p[1]:
                flag = 1
                break
        if flag:
            continue
        g.append((a,b))
    return len(g)

print(m())