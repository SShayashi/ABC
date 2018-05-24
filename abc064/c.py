
def m():
    n = int(input())
    a = list(map(int, input().split()))
    ans = set()
    freecont = 0
    for i in range(n):
        t = a[i] // 400
        if t >= 8:
            freecont+=1
            continue
        ans.add(t)

    return "{} {}".format(max(len(ans),1), len(ans) +freecont)

print(m())