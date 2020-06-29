
def m():
    S = input()
    N = len(S)
    A = [0] * N
    cnt = 0
    for i in range(0, N):
        if S[i] == 'R':
            cnt +=1
        else:
            A[i] = cnt
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt +=1
        else:
            A[i] = cnt
            cnt = 0
    left = 0
    while left < N-1:
        if A[left] == 0:
            left +=1
            continue
        l = A[left] // 2 + A[left+1] // 2 + (A[left+1] % 2)
        r = A[left] // 2 + A[left+1] // 2 + (A[left] % 2)
        A[left] = l
        A[left+1] = r
        left+=2
    for i in range(N):
        print(A[i], end=' ')
    return


m()