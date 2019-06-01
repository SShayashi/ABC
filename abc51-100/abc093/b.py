def main():
    A, B, K = map(int, input().split())
    r = set()
    for i in range(A, A + K):
        if A <= i and B >= i:
            r.add(i)

    for i in range(B, B - K, -1):
        if A <= i and B >= i:
            r.add(i)
    O = list(r)
    O.sort()
    for o in O:
        print(o)


main()
