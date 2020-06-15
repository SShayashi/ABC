def m():
    N = int(input())
    S = [input() for _ in range(N)]
    A = B = C = 0
    ans = 0
    for s in S:
        ans += s.count('AB')
    for s in S:
        if s[0] == 'B' and s[-1] == 'A':
            C += 1
        elif s[0] == 'B':
            B += 1
        elif s[-1] == 'A':
            A += 1
        else:
            pass
    if C == 0:
        return ans + min(A, B)
    ans += C - 1

    if A > 0:
        A -= 1
        ans += 1
    if B > 0:
        B -= 1
        ans += 1
    ans += min(A,B)
    return ans


print(m())
