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

def after_explain():
    d, g = map(int, input().split())
    a = []
    b = []
    for i in range(d):
        p, c = map(int, input().split())
        a.append(p)
        b.append(c)

    mincnt = 999999999
    for i in range(1 << 2 * d):
        score = 0
        cnt = 0
        for j in range(d):
            if i & (1 << j):
                score += a[j]*(j+1)*100 + b[j]
                cnt += a[j]

        for j in range(d-1, -1, -1):
            if not(i & (1 << j)):
                if score > g:
                    break
                s = g - score
                if s % ((j+1)*100) == 0:
                    c = min(a[j], s // ((j + 1) * 100))
                    cnt += c
                    score += c * ((j + 1) * 100)
                else:
                    c = min(a[j], s // ((j + 1) * 100))
                    cnt += c + 1
                    score += (c+1) * ((j + 1) * 100)
                break
        if score < g:
            continue
        if cnt < mincnt:
            mincnt = cnt
    return mincnt

print(after_explain())