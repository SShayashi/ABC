import math
MOD = 10 ** 9 + 7


def main():
    n, m = map(int, input().split())
    total =math.factorial(n+m)
    if abs(n-m) >= 2:
        return 0
    if abs(n-m) == 1:
        return math.factorial(n) * math.factorial(m) % MOD
    return math.factorial(n) * math.factorial(m) * 2 % MOD
print(main())