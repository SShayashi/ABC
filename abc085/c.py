N, Y = [int(i) for i in input().split()]


def f(x, y, z):
    return 10000 * x + 5000 * y + 1000 * z


def b():
    for x in range(N + 1):
        for y in range(N + 1):
            z = N - x - y
            if z < 0:
                continue
            if f(x, y, z) == Y:
                print('{0} {1} {2}'.format(x, y, z))
                return
    print('-1 -1 -1')
    return


b()
