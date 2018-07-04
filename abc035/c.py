def m():
    n, q = map(int, input().split())
    ans = '0b' + ('0' * n)
    for _ in range(q):
        l, r = map(int, input().split())
        tmp = '0b' + ('0' * (l-1)) + ('1' * (r-l+1)) + ('0' * (n-r))
        ans = bin(eval(ans) ^ eval(tmp))
    if len(ans[2:]) < n:
        return '0' * (n - len(ans[2:])) + ans[2:]
    return ans[2:]
print(m())