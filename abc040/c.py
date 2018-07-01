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

def ans():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = abs(a[0]-a[1])
    for i in range(2, n):
        x = dp[i-2] + abs(a[i-2]-a[i])
        y = dp[i-1] + abs(a[i-1]-a[i])
        dp[i] = min(x,y)
    return dp[n-1]
print(ans())