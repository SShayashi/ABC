def m():
    n, q = map(int, input().split())
    ans = 0
    for _ in range(q):
        l, r = map(int, input().split())
        tmp = ((1 << r - l + 1) - 1) * (1 << (n - r))
        ans = ans ^ tmp
    s = bin(ans)
    if len(s[2:]) < n:
        return '0' * (n - len(s[2:])) + s[2:]
    return s[2:]


print(m())
