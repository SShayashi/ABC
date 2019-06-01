def m():
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    if N == 1:
        return abs(a[0] - W)
    return max(abs(a[N - 1] - a[N - 2]), abs(a[N - 1] - W))


print(m())
