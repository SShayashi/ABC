def m():
    n = int(input())
    ans = 0
    for i in range(1, 101):
        if i % n == 0:
            ans += 1
    return 100 - ans

print(m())