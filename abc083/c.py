X, Y = map(int, input().split())

def main():
    x = []
    x.append(X)
    for i in range(Y):
        a = max(x)
        b = a*2
        if b > Y: return print(len(x))
        x.append(b)

main()
