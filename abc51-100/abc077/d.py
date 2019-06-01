def m():
    def solve(p):
        a = 0
        while p != 0:
            a += p % 10
            p //= 10
        return a
    k = int(input())
    MAX = solve(k)
    ans = 9999999999
    for i in range(1, 9):
        ans = min(ans, solve(k*i))

    return ans

print(m())