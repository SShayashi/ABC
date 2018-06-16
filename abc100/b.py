def m():
    d, n = map(int, input().split())
    if d == 0:
        if n == 100:
            return 101
        return n
    if n == 100:
        return (100 **d)*(n+1)
    return (100 **d)*n


print(m())