def m():
    a, b = map(int, input().split())
    # 0は白，1は黒
    grid = [[0]*100 for _ in range(100)]
    k = 50
    for i in range(k):
        for j in range(k*2):
            grid[i][j] = 1

    for i in range(k-1):
        if i % 2 == 0:ind = 0
        else:continue

        while ind < 100 and a-1 > 0:
            grid[i][ind] = 0
            ind += 2
            a -= 1
        if a-1 <= 0:
            break

    for i in range(k*2-1, k,-1):
        if i % 2 == 1:ind = 1
        else:continue

        while ind < 100 and b-1 > 0:
            grid[i][ind] = 1
            ind += 2
            b -= 1
        if b-1 <= 0:
            break

    print("100 100")
    for i in range(k*2):
        for j in range(k*2):
            if grid[i][j] == 0:
                print(".", end="")
            else:
                print("#", end="")
        print("")
m()