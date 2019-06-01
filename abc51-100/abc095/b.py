def m():
    N, X = map(int, input().split())
    M = [int(input()) for m in range(N)]
    a = X - sum(M)
    b = min(M)
    c = a // b
    return c + len(M)

print(m())