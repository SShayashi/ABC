def m():
    n, a = map(int, input().split())
    x = list(map(int, input().split()))
    same = x.count(a)
    under = [k for k in x if k > a]
    over = [k for k in x if k < a]

    for i in range(n):
        for j in range(n):
            pass
    pass

print(m())