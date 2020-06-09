def m():
    N = int(input())
    B = list(map(int, input().split()))
    ans = []
    while B:
        f = True
        for i in reversed(range(len(B))):
            if B[i] == i+1:
                B.pop(i)
                ans.append(i+1)
                f = False
                break
        if f: return print('-1')
    ans.reverse()
    for i in ans:
        print(i)
    return


m()
