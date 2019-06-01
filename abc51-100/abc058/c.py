def m():
    n = int(input())
    s = [str(input()) for _ in range(n)]
    mins = ""

    # 一番小さい文字列取得
    tmp = 9999999
    for i in range(n):
        if len(s[i]) <= tmp:
            tmp = len(s[i])
            mins = s[i]

    d = dict()
    for k in mins:
        d[k] = 0

    #
    for c in mins:
        flag = 0
        for i in range(n):
            if not(c in s[i]):
                flag = 1
                break
        if flag:
            continue
        d[c] += 1

    ans = ""
    for k in sorted(d.keys()):
        ans += k * d[k]
    return ans


import copy

n = int(input())
s = []

for i in range(n):
    s.append(list(input()))

shared = copy.deepcopy(s[0])
for si in s:
    tmp = copy.deepcopy(shared)
    tmp2 = []
    for c in si:
        if c in tmp:
            tmp2.append(c)
            tmp.remove(c)
    shared = copy.deepcopy(tmp2)

for c in sorted(shared):
    print(c, end='')

print()

