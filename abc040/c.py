def m():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    cost = 0
    while i < n:
        x = abs(a[i] - a[i+2])
        y = abs(a[i]-a[i+1]) + abs(a[i+1] - a[i+3])
        if x > y:
            cost += y
            i += 3
        else:
            cost += x
            i += 2

        if (n-i) == 3:
            v = abs(a[i] - a[i+1])
            w = abs(a[i] - a[i+1]) + abs(a[i+1]-a[i+2])
            cost += min(v,w)
            break
        if (n-i) == 2:
            cost += abs(a[i] - a[i+1])
            break
    return cost
print(m())