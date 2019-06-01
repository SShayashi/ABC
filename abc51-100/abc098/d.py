def m():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    left = 0
    right = n
    ans = 0
    for l in range(1, n + 1):
        tmp = a[l]
        for i in a[l + 1:right + 1]:
            tmp = tmp ^ i
        s = sum(a[l:right + 1])
        if tmp == s:
            ans += 1
            ans += abs(l - right)
    return ans


def someone_ans():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    r = 0
    xor_tmp = 0
    sum_tmp = 0
    for l in range(n):
        while r < n and (xor_tmp ^ a[r] == sum_tmp + a[r]):
            xor_tmp = xor_tmp ^ a[r]
            sum_tmp = sum_tmp + a[r]
            r += 1
        xor_tmp = xor_tmp ^ a[l]
        sum_tmp = sum_tmp - a[l]
        ans += r - l
    return ans

# print(m())
print(someone_ans())
