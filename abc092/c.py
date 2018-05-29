def m():
    n = int(input())
    a = list(map(int, input().split()))
    total = abs(a[0]) + abs(a[n-1])
    for i in range(1, n):
        total += abs(a[i] - a[i-1])

    return total


print(m())
