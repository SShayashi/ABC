def m():
    N = int(input())
    X = input()
    R = list(reversed(X))

    memo = [-1] * (N+2)
    for i in range(1, N+2):
        p = 0
        k = i
        while k != 0:
            if memo[k] != -1:
                p += memo[k]
                break

            if k % 2 == 1:
                p+=1
            k //= 2
        memo[i] = p

    def f(n):
        r = 0
        while n != 0:
            n = n % memo[n]
            r += 1
        return r

    memo2 = [0] * (N+2)
    for i in range(1, N+2):
        memo2[i] = f(i)


    total = 0
    for i in range(N):
        total += int(R[i]) * pow(2, i)

    base = X.count('1')
    for i in range(N):
        ans = 0
        if X[i] == '1':
            tmp = total - pow(2, N - 1 - i)
            if (base-1) == 0:
                print(0)
                continue
            tmp %= (base - 1)
            ans = memo2[tmp] + 1
        else:
            tmp = total + pow(2, N - 1 - i)
            tmp %= (base + 1)
            ans = memo2[tmp] + 1
        print(ans)


m()
