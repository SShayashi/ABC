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
    l.sort(reverse=True)
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2,n+1):
        cnt = 999999999
        p = dp[i-1]
        for k in l:
            if (i % k) == 0:
                cnt = i // k
                break
        dp[i] = min(cnt, dp[i-1]+1)
    return dp[n]

print(m())