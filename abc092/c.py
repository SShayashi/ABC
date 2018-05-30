def m():
    n = int(input())
    a = list(map(int, input().split()))
    total = abs(a[0]) + abs(a[n-1])
    for i in range(1, n):
        total += abs(a[i] - a[i-1])
    for j in range(n):
        if j == 0:
            print(total - abs(a[j]) - abs(a[j]-a[j+1]) + abs(a[j+1]))
            continue
        if j == n-1:
            print(total - abs(a[j-1]-a[j]) - abs(a[j]) + abs(a[j-1]))
            continue
        print(total - abs(a[j-1]-a[j]) - abs(a[j]-a[j+1]) + abs(a[j+1]-a[j-1]))


m()
