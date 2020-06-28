def m():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        n = N//i
        ans += (n * (n + 1) // 2)*i
    return ans


print(m())
