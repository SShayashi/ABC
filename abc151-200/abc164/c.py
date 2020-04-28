def m():
    n = int(input())
    d = {}
    for _ in range(n):
        d[str(input())] = 1
    return len(d.keys())


print(m())
