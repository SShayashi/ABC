def m():
    A, B, C, D, E, F = map(int, input().split())

    ans = 0
    for i in range(1, F):
        for k in range(1, F):
            x = A * 100 * i + B * 100 * k
            y = C * i + D * k
            if x / 100 >= E * y:
                ans = max((100 * x) / (x + y), ans)
    return ans

print(m())
