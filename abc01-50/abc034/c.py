from math import factorial
mod = 1000000007


def m():
    w, h = map(int, input().split())
    ans = factorial(w+h-2)*pow(factorial(w-1), mod-2, mod) * pow(factorial(h-1), mod-2, mod)
    return ans % mod

print(m())