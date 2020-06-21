def m():
    N, K = map(int, input().split())
    S = input()
    comp = []
    prev = S[0]
    cnt = 1
    for i in range(1, N):
        if prev == S[i]:
            cnt += 1
            prev = S[i]
        else:
            comp.append(cnt)
            prev = S[i]
            cnt = 1
    comp.append(cnt)
    comp_n = len(comp)
    acum = [0] * (comp_n + 1)
    acum[0] = 0
    if comp_n < (2*K):
        return N
    for i in range(comp_n):
        acum[i + 1] = comp[i] + acum[i]
    ans = 0
    if S[N - 1] == '0':
        ans = max(acum[comp_n] - acum[comp_n - (2 * K)], ans)

    if S[0] == '0':
        ans = max(acum[2 * K], ans)
    left = 1 if S[0] == '0' else 0
    right = left + (K*2+1)
    while right <= comp_n:
        t = acum[right] - acum[left]
        ans = max(ans, t)
        right +=2
        left +=2
    return ans


print(m())
