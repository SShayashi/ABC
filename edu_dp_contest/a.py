def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cost = [0 for _ in range(n)]
    for i in range(1, n):
        m = float('inf')
        for j in range(1, k+1):
            if (i - j) < 0:
                break
            m = min(m, cost[i-j] + abs(h[i] - h[i - j]))
        cost[i] = m
    return cost[n - 1]


print(main())
