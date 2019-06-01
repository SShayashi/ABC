def is_odd(num):
    return num % 2 == 1

def m():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    n = 0
    ans = []
    for i in range(h):
        for j in range(w-1):
            if is_odd(a[i][j]):
                a[i][j] -=1
                a[i][j+1] += 1
                n += 1
                ans.append((i,j,i,j+1))
    for i in range(h-1):
        if is_odd(a[i][w-1]):
            a[i][w-1] -=1
            a[i+1][w-1] -= 1
            n += 1
            ans.append((i, w-1, i+1, w-1))

    print(n)
    for i in range(n):
        print(ans[i][0]+1, ans[i][1]+1, ans[i][2]+1, ans[i][3]+1)


m()