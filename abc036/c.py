def m():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    b = [0] * n
    s = list(set(a))
    s.sort()
    d = dict()
    for i in range(len(s)):
        d[s[i]] = i
    for i in range(n):
        b[i] = d[a[i]]
    for i in range(n):
        print(b[i])
m()