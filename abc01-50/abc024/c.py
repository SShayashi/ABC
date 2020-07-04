def m():
    N, D, K = map(int, input().split())
    LR = []
    for _ in range(D):
        l, r = map(int, input().split())
        LR.append([l, r])
    ST = []
    for _ in range(K):
        s, t = map(int, input().split())
        ST.append([s, t])

    for k in range(K):
        s, t = ST[k]
        ans = 0
        for i in range(D):
            l, r = LR[i]
            if l <= s <= r:
                if l <= t <= r:
                    ans = i
                    break
                if s < t:
                    s = r
                else:
                    s = l
        print(ans+1)
    return


m()
