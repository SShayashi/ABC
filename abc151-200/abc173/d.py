from collections import Counter

def m():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    c = Counter(A[1:])
    d = list(c.items())
    d.sort(reverse=True, key=lambda x:x[0])
    tmp = []
    for k,v in d:
        for i in range((v-1)+(v+1)):
            tmp.append(k)
    ans += sum(tmp[:N-2])
    return ans
print(m())