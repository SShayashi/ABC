def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    MAX = 9999999
    for a in A:
        B[a] += 1
    kinds = 0
    for b in B:
        if b != 0:
            kinds +=1
    if kinds <= K:
        return 0
    diff = kinds - K
    ans = 0
    for d in range(diff):
        m = 9999999
        index = 0
        for i, v in enumerate(B):
            if v == 0:
                continue
            m = min(m, v)
            index = i
        B[index] = 9999999
        ans += m
    return ans


print(main())
