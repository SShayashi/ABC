
def m():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0 ,0)
    left = 0
    right = n-1
    ans = 0
    for l in range(1, n+1):
        for r in range(n, l-1, -1):
            tmp = a[l]
            for i in a[l+1:r+1]:
                tmp = tmp ^ i
            s = sum(a[l:r+1])
            if tmp == s:
                ans += 1
                ans += abs(l-r)
                break
    return ans
print(m())