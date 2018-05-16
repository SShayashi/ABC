def m():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = []
    T.sort()
    for i in range(len(T)):
        tmp = T[i]
        flag = 0
        for k in range(i+1, len(T)):
            if T[k] % tmp == 0:
                flag = 1
                break
        if flag == 0:
            ans.append(tmp)
    ans = set(ans)
    a = 1
    for j in ans:
        a *= j
    return a

print(m())