def m():
    a, b, n = map(int, input().split())

    def calc(x):
        return int((a * x) / b) - (a * int(x / b))

    return calc(min(n, b-1))

print(m())
