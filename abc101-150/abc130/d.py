def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    acum = [0] * n
    acum[0] = a[0]
    for i in range(1, n):
        acum[i] = a[i] + acum[i - 1]
    left = right = ans = 0
    while left < n:
        diff =(acum[right] - acum[left])
        if diff >= k:
            ans += (n-right)
            left+=1
            right = left
        elif diff < k:
            right+=1
    return ans

print(m())

