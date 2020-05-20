def m():
    d = dict(zip(list(map(int, input().split())), [i for i in range(10)]))
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = [[0, 0] for _ in range(n)]
    for j in range(n):
        score = 0
        tmp = a[j]
        base = 1
        while tmp:
            score += d[tmp % 10] * base
            tmp //= 10
            base *= 10
        ans[j][0] = a[j]
        ans[j][1] = score
    ans.sort(key=lambda x:x[1])
    for k in ans:
        print(k[0])
    return


m()
