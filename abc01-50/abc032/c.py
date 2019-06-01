def m():
    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    if 0 in s:
        return n

    left = 0
    right = 0
    ans = 0
    tmp = s[right]
    while right < n:
        if tmp <= k:
            ans = max(ans, right-left+1)
            right += 1
            if right !=n:
                tmp *= s[right]
        else:
            tmp //= s[left]
            left += 1

        if left > right:
            right = left
            if right == n:
                break
            tmp = s[right]
    return ans

print(m())