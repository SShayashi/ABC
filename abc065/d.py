def main():

    def prime():
        visited = []

        pass

    n = int(input())
    X, Y = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append((x,y))
        Y.append((x,y))
    X.sort(key=lambda x:x[0])
    Y.sort(key=lambda x:x[1])
    l = list(zip(X,Y))



print(main())