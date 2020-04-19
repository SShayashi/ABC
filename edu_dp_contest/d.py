def main():
    n, mw = map(int, input().split())
    a = []
    for _ in range(n):
        w, v = map(int, input().split())
        a.append([w, v])
    dp = [[0 for _ in range(n)] for _ in range(mw)]
    for i in range(1, mw):
        for k in range(n):
            if a[k][0] <= k:
                dp[i]
            pass
        pass

    for k in range(n):
        pass
    for i in range(1, mw):
        mini = float('inf')
        point = -1
        for k in range(n):
            if a[k][0] < mini:
                point = k
        dp[a[point][0]] = a[point]

        pass


main()
