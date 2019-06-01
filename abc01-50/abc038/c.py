def m():
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    right = 1
    ans = 0
    while right < n:
        if a[right-1] < a[right]:
            right+=1
            continue

        if left-right == 1:
            ans += 1
            continue
        d = right - left
        ans += d * (d+1) // 2
        left = right
        right += 1

    if left - right == 1:
        ans += 1
        return ans

    d = right - left
    ans += d * (d + 1) // 2
    return ans

print(m())