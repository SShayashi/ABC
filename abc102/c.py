def m():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in range(1, n+1):
        cnt += a[i-1]-i
    b = cnt // n
    for j in range(1, n+1):
        ans += abs(a[j-1]-(b+j))
    return ans

print(m())