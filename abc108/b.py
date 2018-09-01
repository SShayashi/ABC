def m():
    a, b, c, d = map(int, input().split())
    x = c-a
    y = d-b
    return "{} {} {} {}".format(c-y,d+x, a-y,b+x)


print(m())