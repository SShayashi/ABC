def m():
    N = int(input())
    M = 100
    dp = [[[0] for _ in range(M)] for _ in range(M)]
    ANS = [0] * (N+1)
    for i in range(1, M+1):
        for j in range(1, M+1):
            for k in range(1, M+1):
                a = pow(i,2) + pow(j,2) + pow(k,2)
                b = i*j + j*k + k*i
                tmp = a + b
                if tmp > N:
                    continue
                ANS[tmp] +=1
    for i in range(1, N+1):
        print(ANS[i])
m()