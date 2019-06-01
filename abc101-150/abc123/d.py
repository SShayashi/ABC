x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

def m():
    a = []
    b = []
    c = []
    cnt = [0,0,0]

    for i in range(k):
        if A[cnt[0]] >= B[cnt[1]] and A[cnt[0]] >= C[cnt[2]]:
            a.append(A[cnt[0]])
            cnt[0] += 1
            continue
        if B[cnt[1]] >= A[cnt[0]] and B[cnt[1]] >= C[cnt[2]]:
            b.append(B[cnt[1]])
            cnt[1] += 1
            continue
        if C[cnt[2]] >= A[cnt[0]] and C[cnt[2]] >= B[cnt[1]]:
            c.append(C[cnt[2]])
            cnt[2] += 1
            continue
    ans = []
    for i in range(len(a)):
        for j in range(len(b)):
            for p in range(len(c)):
                ans.append(a[i]+b[j]+c[p])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

m()
