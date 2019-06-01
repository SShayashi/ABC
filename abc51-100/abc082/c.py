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
        if B[i] == i:
            continue
        elif B[i] > i:
            total += B[i] - i
        else:
            total += B[i]
    print(total)
main()
