def m():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    B = [a[i-1]-i for i in range(1, n+1)]
    B.sort()
    b = B[n//2]
    for i in range(n):
        ans += abs(B[i]-b)
    return ans

print(m())