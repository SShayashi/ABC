def m():
    n = int(input())
    a = [["." for _ in range(n)] for _ in range(n)]
    flag = 1
    for i in range(0, n, 2):
        flag ^= 1
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == flag:
                    a[i][j] = "X"
    if n % 2 == 0:
        if a[n-2][0] == "X":
            for i in range(n-2, -1, -4):
                a[n-1][i] = "X"
        else:
            for i in range(1, n, 4):
                a[n - 1][i] = "X"
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == "X":
                cnt += 1
            print(a[i][j], end="")
        print("")
    print(cnt)
m()