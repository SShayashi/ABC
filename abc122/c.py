N, Q = map(int, input().split())
S = input()
l, r = [],[]
for _ in range(Q):
    x, y = map(int, input().split())
    l.append(x)
    r.append(y)

def m():
    t = [0] * len(S)
    ans = [0] * len(S)
    prev = S[0]
    for i in range(1, len(S)):
        if prev != 'A':
            prev = S[i]
            continue
        if S[i] == 'C':
            t[i] += 1
        prev = S[i]
    ans[0] = t[0]
    for i in range(1, len(t)):
        ans[i] = ans[i-1] + t[i]

    for i in range(Q):
        print(ans[r[i]-1] - ans[l[i]-1])

m()