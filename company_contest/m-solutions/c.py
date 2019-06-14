from math import factorial


def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def solve(start, end):
    s = 0
    for i in range(end-start):
        s += 0.5**(start-1)*nCr(start,i)*2
    return s