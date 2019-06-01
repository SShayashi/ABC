def m():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    tmp = -1
    cnt = 0
    ans = 0
    for i in range(N):
        if tmp == A[i]:
            cnt +=1
        else:
            if cnt % 2 == 0: pass
            else: ans +=1
            tmp = A[i]
            cnt = 1

    if cnt % 2 == 0: pass
    else: ans += 1
    return ans

print(m())
