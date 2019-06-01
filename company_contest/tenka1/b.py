N = int(input())
S = input()
K = int(input())

def m():
    p = S[K-1]
    ans = ''
    for i in range(N):
        if p != S[i]:
            ans += '*'
        else:
            ans += S[i]
    return ans
print(m())