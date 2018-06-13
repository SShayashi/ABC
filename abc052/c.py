MOD = 10 ** 9 + 7

def get_prime_array(N):
    f = []
    for i in range(2, N + 1):
        flag = 0
        for j in f:
            if i % j == 0:
                flag = 1
                break
        if flag:
            continue
        f.append(i)
    return f


def m():
    n = int(input())
    d = dict()
    prime = get_prime_array(n)
    for i in range(2,n+1):
        tmp = i
        for p in prime:
            while not (tmp == 1):
                if tmp % p == 0:
                    tmp //= p
                    if d.get(p, 0) == 0:
                        d[p] = 1
                    else:
                        d[p] +=1
                else:
                    break
    ans = 1
    for k in d.keys():
        ans *= (d[k]+1)
    return ans % MOD
print(m())
