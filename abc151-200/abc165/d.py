def m():
    a, b, n = map(int, input().split())

    def calc(x):
        return int((a * x) / b) - (a * int(x / b))

    if calc(1) < calc(n // 2):
        return max([calc(i) for i in range(n // 2, n + 1)])
    else:
        return max([calc(i) for i in range(1, n // 2 + 1)])


print(m())
