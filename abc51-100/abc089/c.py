def m():
    n = int(input())
    S = [str(input()) for _ in range(n)]
    m = 0
    a = 0
    r = 0
    c = 0
    h = 0
    x = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
    y = [1, 1, 1, 2, 2, 3, 2, 2, 3, 3]
    z = [2, 3, 4, 3, 4, 4, 3, 4, 4, 4]
    for i in range(n):
        if S[i][0] == "M":
            m += 1
        elif S[i][0] == "A":
            a += 1
        elif S[i][0] == "R":
            r += 1
        elif S[i][0] == "C":
            c += 1
        elif S[i][0] == "H":
            h += 1
    ans = 0
    d = [m, a, r, c, h]
    for j in range(10):
        ans += d[x[j]] * d[y[j]] * d[z[j]]
    return ans
print(m())
