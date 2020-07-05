def m():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    plus = []
    minas = []
    MOD = 10 ** 9 + 6
    for a in A:
        if a >= 0:
            plus.append(a)
        else:
            minas.append(a)
    plus.sort(reverse=True)
    minas.sort()
    p_l = len(plus)
    m_l = len(minas)
    PR = [0] * (p_l+1)
    MR = [0] * (m_l+1)
    PR[0] = 1
    MR[0] =  1
    for i in range(p_l):
        PR[i + 1] = (PR[i] * plus[i])
    for i in range(m_l):
        MR[i + 1] = (MR[i] * minas[i])

    pi = len(PR) - 1 if len(PR) <= K else K
    for a in range(K-pi, -1, -1):
        ans = max(MR[a]*AR, ans)
    return pi


print(m())
