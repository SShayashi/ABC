def m():
    a, b = map(int, input().split())
    return max(a+b, a-b, a*b)

print(m())