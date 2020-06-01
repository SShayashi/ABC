def m():
    N = int(input())
    XL = [list(map(int, input().split())) for _ in range(N)]
    ST = [[xl[0] - xl[1], xl[0] + xl[1]] for xl in XL]
    ST.sort(key=lambda x: x[1])
    ans = 1
    right = ST[0][1]
    for i in range(1, N):
        if right <= ST[i][0]:
            right = ST[i][1]
            ans += 1
    return ans


print(m())
