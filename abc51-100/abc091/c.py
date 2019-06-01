def m():
    n = int(input())
    red = [list(map(int, input().split())) for _ in range(n)]
    blue = [list(map(int, input().split())) for _ in range(n)]
    red.sort(key=lambda x: x[1], reverse=True) # yの大きい順
    blue.sort(key=lambda y: y[0]) # xの小さい順
    ans = 0
    for b in blue:
        for r in red:
            if r[0] < b[0] and r[1] < b[1]:
                red.remove(r)
                ans +=1
                break
    return ans

print(m())
