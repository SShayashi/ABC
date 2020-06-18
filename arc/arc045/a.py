import itertools


def m():
    S = input()
    ans = 0
    for i in range(len(S)):
        for item in itertools.combinations(range(len(S) - 1), i):
            if len(item) == 0:
                ans += int(S)
                continue
            ind = 0
            for j in item:
                ans += int(S[ind:j+1])
                ind = j+1
            ans += int(S[ind:])
    return ans


print(m())
