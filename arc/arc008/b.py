from math import ceil
from collections import Counter


def m():
    N, M = map(int, input().split())
    S = Counter(str(input()))
    K = Counter(str(input()))
    ans = 1
    for k, v in S.items():
        if K.get(k, None) is None:
            return -1
        if S[k] > K[k]:
            ans = max(ans, ceil(S[k]/K[k]))
    return ans
print(m())
