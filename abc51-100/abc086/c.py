def m():
    n = int(input())
    nowt = 0
    nowx = 0
    nowy = 0
    for i in range(n):
        t, x, y = map(int, input().split())
        divt = abs(nowt - t)
        divx = abs(nowx - x)
        divy = abs(nowy - y)
        if divt < divx + divy:
            return "No"
        if divt == divx + divy:
            continue
        if (divt - divx + divy) % 2 == 0:
            continue
        return "No"
    return "Yes"

print(m())
