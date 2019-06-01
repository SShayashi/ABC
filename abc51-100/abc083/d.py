def main():
    S = input()
    N = len(S)
    for k in range(N - 1, (N // 2) - 1, -1):
        first = S[0:k]
        union = k * 2 - N
        cut = first[-union:-1] + first[-1]
        if '1' in cut and '0' in cut:
            continue
        else:
            return print(k)


def ans():
    S = input()
    N = len(S)
    if not ('1' in S and '0' in S):
        return print(N)

    tmp = 1000000
    for i, v in enumerate(S):
        if i == 0:
            continue
        if S[i-1] != v:
            tmp = min(max(i, N-i), tmp)
    return print(tmp)

# main()
ans()