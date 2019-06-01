MAX = 10 ** 10
def m():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1,n):
        a[i] += a[i-1]
    ans = MAX
    left_i = 0
    right_i = 2
    for mid in range(1,n-2):
        while left_i < mid and abs(a[left_i+1] - (a[mid]-a[left_i+1])) < abs(a[left_i] - (a[mid]-a[left_i])):
            left_i += 1

        if right_i <= mid:
            right_i = mid+1

        while right_i < n-1 and abs((a[right_i+1] - a[mid]) - (a[n-1] - a[right_i+1])) < abs((a[right_i] - a[mid]) - (a[n-1] - a[right_i])):
            right_i += 1
        p = a[left_i]
        q = a[mid] - a[left_i]
        r = a[right_i] - a[mid]
        s = a[n-1] - a[right_i]
        ans = min(ans, max(p,q,r,s) - min(p,q,r,s))
    return ans

print(m())