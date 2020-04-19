def main():
    MOD = 10 ** 9 + 7
    n, k = map(int, input().split())
    a = list(range(n + 1))
    x = a.copy()
    y = a.copy()
    ans = 0
    for i in range(1, n+1):
        x[i] = a[i] + x[i-1]

    for i in range(n-1, -1, -1):
        y[i] = a[i] + y[i+1]

    for j in range(k-1, n+1):
        ans += y[-j-1] - x[j] + 1
    return ans%MOD


print(main())
