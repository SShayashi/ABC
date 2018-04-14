def m():
    N = int(input())
    X = [int(x) for x in input().split()]
    XX = [x for x in X]
    XX.sort()
    first = XX[N//2]
    second = XX[N//2 -1]
    for x in range(N):
        if X[x] <= second:
            print(first)
        else:
            print(second)


m()
