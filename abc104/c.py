def m():
    d, g = map(int, input().split())
    a = []
    b = []
    for i in range(d):
        p, c = map(int, input().split())
        per = (100*(i+1) * p + c) // p
        a.append((per, i, p, c))
        b.append((i, p))
    a.sort(reverse=True, key=lambda x: x[0])
    b.sort(reverse=True, key=lambda y: y[1])
    cnt = 0
    used = []
    for i in range(d):
        per, key, p, nus = a[i]
        for j in range(p):
            g -= 100*(key+1)
            cnt += 1
            if g <= 0:
                return cnt
        g -= nus
        if g <= 0:
            return cnt
        for k in range(d):
            if b[k][0] == key:
                b.remove(b[k])
                break

print(m())