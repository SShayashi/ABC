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

    def calory(a, b):
        craitrin = C // 2
        cost = 0
        if a == b:

            cost += min(a,b)

        if X[a] < craitrin: cost += Vsum[a]
        else: cost += Vsum[-1] - Vsum[a]

        if X[b] < craitrin: cost += Vsum[b]
        else: cost += Vsum[-1] - Vsum[b]

        return cost

    for a in range(N):
        for b in range(N):
            A = X[a]
            B = X[b]
            dp[a][b] = calory(a, b)

    tmp = -9999999
    for a in range(N):
        for b in range(N):
            tmp = max(tmp, dp[a][b] - distance(a,b))

    return tmp


def someone_ans():
    N, C = map(int, input().split())
    X=[]
    V=[]
    for _ in range(N):
        x, v = map(int, input().split())
        X.append(x)
        V.append(v)

    rev_V = V[::-1]
    rev_X = tuple(map(lambda x: C-x, X[::-1]))
    a1 = solve(N, X, V, rev_X, rev_V)
    a2 = solve(N, rev_X, rev_V, X, V)
    ans = max(a1,a2)
    return ans

def solve(N, X, V, rev_X, rev_V):
    ans = 0
    for i in range(N):
        a = sum(V[:i+1]) - X[i]
        ans = max(ans, a)
        a = max(a - X[i], 0)
        for k in range(N-i-1):
            b = a + sum(rev_V[:k+1]) - rev_X[k]
            ans = max(ans, b)
    return ans

# m()
# print(ans())
print(someone_ans())