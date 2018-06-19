def m():
    n = int(input())
    tt, aa = map(int, input().split())
    for _ in range(n-1):
        t, a = map(int, input().split())
        if t == a:
            tt = max(tt, aa)
            aa = max(tt, aa)
        elif t > a:
            if aa % a == 0:
                pass
            else:

            tt = int(aa * (t / a))
        else:
            aa = int(tt * (a / t))
    return aa + tt

print(m())
