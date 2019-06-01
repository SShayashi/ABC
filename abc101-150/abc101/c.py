def m():
    def solve(n,k):
        if n <= k:
            return 1
        tmp = 1
        tmp += (n-k) // (k-1)
        if (n-k) % (k-1) == 0:
            return tmp
        return tmp + 1

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    pos = a.index(1)
    ans = 1
    if pos <= (k-1) or pos >= (n-k):
        return solve(n,k)
    if (k % 2) == 0:
        div = k // 2
        left = a[:pos+(div-1)]
        right = a[pos+(div-1):]
    else:
        div = k // 2
        left = a[:pos+(div-1)]
        right = a[pos+(div):]
    ans += solve(len(left), k) + solve(len(right),k)
    return ans
print(m())
