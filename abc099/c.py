def m():
    n = int(input())
    a = set()
    for i in range(100):
        tmp = 9 ** i
        if tmp > 100000:
            break
        a.add(tmp)
    for i in range(100):
        tmp = 6 ** i
        if tmp > 100000:
            break
        a.add(tmp)
    l = list(a)
    l.sort()
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        b = []
        for j in l:
            if j > i:
                break
            b.append(1 + dp[i-j])
        dp[i] = min(b)
    return dp[n]

print(m())