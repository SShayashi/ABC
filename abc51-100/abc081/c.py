def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    MAX = 9999999
    for a in A:
        B[a] += 1
    B.sort(reverse=True)
    s = 0
    for i in range(0, K):
        s += B[i]
    return sum(B) - s


print(main())
