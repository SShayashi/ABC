def m():
    n = int(input())
    a = []
    for i in range(3 ** n):
        tmp = ""
        while i != 0:
            tmp = str(i % 3) + tmp
            i //= 3
        p = ((n-len(tmp))*"0") + tmp
        p=p.replace("0","a")
        p=p.replace("1","b")
        p=p.replace("2","c")
        a.append(p)
    a.sort()
    for c in a:
        print(c)

m()