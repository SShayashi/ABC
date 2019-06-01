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


def ans():
    n, q = map(int, input().split())
    a = [0] * (n+2)
    for _ in range(q):
        l, r = map(int, input().split())
        a[l] += 1
        a[r+1] -= 1
    answer = ''
    for i in range(1, n+1):
        a[i] += a[i-1]
        if a[i] % 2 == 0:
            answer += "0"
        else:
            answer += "1"
    return answer


print(ans())
