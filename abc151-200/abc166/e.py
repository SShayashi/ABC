def m():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    length = len(A)
    x = [i - A[i] for i in range(length)]
    y = [i + A[i] for i in range(length)]
    xdict = {}
    ydict = {}
    for i in range(1, length):
        xdict[x[i]] = xdict[x[i]] + 1 if xdict.get(x[i], 0) else 1
        ydict[y[i]] = ydict[y[i]] + 1 if ydict.get(y[i], 0) else 1

    ans = 0
    for k, v in xdict.items():
        ans = ans + ydict[k] * v if ydict.get(k, 0) else ans
    return ans


print(m())
