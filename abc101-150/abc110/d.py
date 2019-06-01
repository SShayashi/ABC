import collections

N, M = map(int, input().split())
MOD = 10 ** 9 + 7


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def comb(n,k,p):
    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % p
    b = factorial(k) % p
    c = factorial(n - k) % p
    # ここで 逆元を求めて，割り算を掛け算に変換している
    # (k!) ** p-2 を求める．これをxとする
    # すると k!で割り算しなければならなかった計算が xを掛けるだけでよくなる．
    #
    return (a * power_func(b, p - 2, p) * power_func(c, p - 2, p)) % p


def power_func(a,b,p):
    if b == 0: return 1
    if b % 2 == 0:
        d = power_func(a, b // 2, p)
        return d * d % p
    if b % 2 == 1:
        return (a * power_func(a, b - 1, p)) % p

def m():
    ans = 1
    f = prime_factors(M)
    counts = collections.Counter(f)
    for k,v in counts.items():
        ans *= comb(v + N-1, N-1, MOD)
    return ans % MOD

print(m())