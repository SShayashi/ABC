def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    alice = sum(A[0::2])
    bob = sum(A[1::2])
    return alice-bob

print(main())