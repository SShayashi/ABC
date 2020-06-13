def m():
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    p = 0
    for b in B:
        f = False
        for i in range(p, N):
            if A[i] <= b <= A[i]+T:
                p = i+1
                f = True
                break
        if not f:
            return 'no'
    return 'yes'
print(m())