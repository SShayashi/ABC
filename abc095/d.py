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

def ans():
    N, C = map(int, input().split())
    X=[]
    V=[]
    dp = [[0]*N]*N
    for _ in range(N):
        x, v = map(int, input().split())
        X.append(x)
        V.append(v)

    def distance(a, b):

        a = min(a, abs(a-C))
        b = min(b, abs(b-C))
        return min(a*2+b,b*2+a)

    Vsum = [0] * N
    Vsum[0] = V[0]
    for i in range(1, N):
        Vsum[i] = Vsum[i-1] + V[i]

    for a in range(N):
        for b in range(N):
            A = X[a]
            B = X[b]
            dp[a][b] = distance(A,B)
    pass


# m()
ans()