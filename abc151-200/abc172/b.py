def m():
    S = input()
    T = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    return ans
print(m())