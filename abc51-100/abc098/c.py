def m():
    n = int(input())
    s = str(input())
    w = 0
    e = 0
    for i in range(n):
        if s[i] == 'W':
            w +=1
        elif s[i] == 'E':
            e +=1

    ans = 99999999999
    lw = 0
    for j in range(n):
        if s[j] == 'W':
            w -= 1
            ans = min(e+lw, ans)
            lw +=1
        if s[j] == 'E':
            e -= 1
            ans = min(e+lw, ans)
    return ans

print(m())