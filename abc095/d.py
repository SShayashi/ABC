def m():
    N, C = map(int, input().split())
    X=[]
    V=[]
    dp = [0] * N
    for _ in range(N):
        x, v = map(int, input().split())
        X.append(x)
        V.append(v)

    def get_route(first, end):
        diff = abs(first-end)
        return min(abs(diff), abs(diff-C))

m()