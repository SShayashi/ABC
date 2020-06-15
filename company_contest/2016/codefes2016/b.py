def m():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    a = A[0]
    b = sum(A[1:])
    if (a-b) <= 1:
        return 0
    else:
        return (a-b)-1


print(m())
