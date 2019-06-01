def m():
    n, m = map(int, input().split())
    bridge = [1 for _ in range(n)]
    g = []
    for _ in range(m):
        a, b = map(int, input().split())
        g.append((a, b))
    g.sort(key=lambda x: x[1])
    cnt = 0
    for e in g:
        f = 0
        for j in range(e[1]-1, e[0]-1, -1):
            if bridge[j] == 0:
                f = 1
                break
        if f:
            continue
        # if bridge[e[0]:e[1]].count(0):
        #     continue
        bridge[e[1]-1] = 0
        cnt += 1
    return cnt

print(m())