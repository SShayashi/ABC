def m():
    n = int(input())
    s = [str(input()) for _ in range(n)]
    mins = ""
    ans = ""
    tmp = 9999999
    for i in range(n):
        if len(s[i]) <= tmp:
            tmp = len(s[i])
            mins = s[i]

    d = dict()
    for k in range(97, 97+26):
        d[chr(k)] = 0

    flag = 0
    for c in mins:
        flag = 0
        for i in range(n):
            if not(c in s[i]):
                flag = 1
                break
        if flag:
            continue
        d[c] += 1

    for k in range(97, 97 + 26):
        for p in range(d[chr(k)]):
            ans += chr(k)
    return ans

print(m())