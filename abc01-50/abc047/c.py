def m():
    s = str(input())
    cnt = 0
    tmp = s[0]
    for i in s:
        if tmp != i:
            tmp = i
            cnt += 1
    return cnt


print(m())