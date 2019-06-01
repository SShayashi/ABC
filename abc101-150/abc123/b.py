def m():
    A = []
    for _ in range(5):
        a = int(input())
        A.append(a)

    amari = 10
    tmp = 0
    for i in range(5):
        if A[i] % 10 == 0:
            continue
        if (A[i] % 10) < amari:
            tmp = i
            amari = A[i] % 10
    if amari == 10:
        return sum(A)
    ans = []
    for i in range(5):
        if i == tmp:
            ans.append(A[tmp])
            continue
        if A[i] % 10 == 0:
            ans.append(A[i])
            continue
        ans.append(A[i] + (10 - A[i]%10))
    return sum(ans)
print(m())