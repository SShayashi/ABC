def m():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    acum = [0] * (n+1)
    acum[0] = 0
    for i in range(n):
        acum[i+1] = a[i] + acum[i]
    left = right = ans = 0
    while left <= n:
        diff = acum[right] - acum[left]
        if diff >= k:
            ans += (n - right)+1
            left += 1

        elif diff < k:
            right += 1
            if right > n:
                return ans

    return ans


print(m())
