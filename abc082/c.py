def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = {}
    total = 0
    for i, a in enumerate(A):
        b = B.get(a, 0)
        if b == 0:
            B[a] = 1
        else:
            B[a] += 1

    for i in B:
        if B[i] == 0:
            continue
        total += min(abs(B[i]-i), B[i])
    print(total)
main()
