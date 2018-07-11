MAX = 10 ** 10
def m():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1,n):
        a[i] += a[i-1]
    ans = MAX
    left_i = 0
    right_i = 2
    for i in range(1,n-2):
        p,q = MAX,MAX
        r,s = MAX,MAX
        left_diff = MAX
        right_diff = MAX
        while left_i < i:
            d = abs(a[left_i] - (a[i]-a[left_i]))
            if d < left_diff:
                left_diff = d
                p = a[left_i]
                q = a[i]-a[left_i]
            else:
                break
            left_i += 1
        left_i -=1

        if right_i <= i:
            right_i = i+1

        while right_i < n:
            d = abs((a[right_i] - a[i]) - (a[n-1] - a[right_i]))
            if d < right_diff:
                right_diff = d
                r = a[right_i] - a[i]
                s = a[n-1] - a[right_i]
            else:
                break
            right_i += 1
        right_i -= 1

        ans = min(ans, max(p,q,r,s) - min(p,q,r,s))
    return ans

print(m())