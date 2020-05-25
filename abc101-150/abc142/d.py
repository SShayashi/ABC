from fractions import gcd
from math import factorial


def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def lcm(x, y):
    return (x * y) // gcd(x, y)


def prime_numbers(n):
    if n < 2:
        return [1]
    primes = []
    for p in range(2, int(pow(n, 0.5)) + 1):
        if p * p > n:
            break
        while n % p == 0:
            primes.append(p)
            n //= p
    if n > 1:
        primes.append(n)
    return primes


def m():
    a, b = map(int, input().split())
    x = gcd(a, b)
    p = prime_numbers(x)
    p.append(1)

    return len((set(p)))


print(m())
