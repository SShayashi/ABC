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


main()
