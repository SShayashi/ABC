NOT_FOUND = 'UNRESTORABLE'


def m():
    S = list(str(input()))
    T = list(str(input()))
    first = 0
    end = 0
    for i in range(len(S) + 1 - len(T)):
        for k in range(len(T)):
            if S[i + k] != T[k] and S[i + k] != '?':
                break
            if k == len(T) - 1:
                first = i
                end = i + k
    if (end - first) < len(T) - 1:
        return NOT_FOUND

    j = 0
    while first <= end:
        S[first] = T[j]
        first += 1
        j += 1
    ans = "".join(S)
    r = ans.replace('?', 'a')
    return r


print(m())
