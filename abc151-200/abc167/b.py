def m():
    a, b, c, k = map(int, input().split())
    ans = 0
    if (k - a) <= 0:
        return k
    k = k - a
    ans = a
    if (k - b) <= 0:
        return ans
    k = k -b
    return ans - k


print(m())
