def m():
    n = int(input())
    L = 32
    a = [0] * L
    b = [0] * L
    b[0], b[1] = 1, -2
    ans = ["0"] * L
    for i in range(L):
        a[i] = (-2) ** i

    for i in range(2, L):
        b[i] = a[i] + b[i-2]
    
    def solve(p):
        if p == 0:
            return
        if p < 0:
            for j in range(1, L, 2):
                if p >= b[j]:
                    p -= a[j]
                    ans[j] = "1"
                    solve(p)
                    break
        else:
            for j in range(0, L, 2):
                if p <= b[j]:
                    p -= a[j]
                    ans[j] = "1"
                    solve(p)
                    break
    solve(n)
    ans.reverse()
    return int("".join(ans))


print(m())