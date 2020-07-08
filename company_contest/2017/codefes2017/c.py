def m():
    S = input()
    N = len(S)
    A = S.replace('x', '')
    B = ''.join(reversed(A))
    M = len(A)
    for i in range(M):
        if A[i] != B[i]: return -1

    half = M // 2 if M % 2 == 0 else M // 2 + 1
    C = A[:half]
    p = 0
    l_center = 0
    for i in range(N):
        if S[i] == C[p]:
            p+=1
        if p >= half:
            l_center = i
            break
    p = 0
    r_center = 0
    for i in range(N-1, -1, -1):
        if S[i] == C[p]:
            p +=1
        if p >= half:
            r_center = i
            break
    l_s = S[:l_center]
    r_s = S[r_center:]

    return l_s, r_s


print(m())